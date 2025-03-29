# 3d

Pure Lua 3D lib for norns.

![teapot](https://www.eigenbahn.com/assets/gif/norns_3d_teapot.gif)


## Description

Provides classes for storing & manipulating 3D objects, with similar APIs but different internal structures:

 - [Polyhedron](./lib/3d/polyhedron.lua)
 - [Wireframe](./lib/3d/wireframe.lua)
 - [Sphere](./lib/3d/sphere.lua)

`Polyhedron` has a notion of faces composed of vertices. It is more suited for importing 3D models.

`Wireframe`, on the other hand, only has a notion of edges (line between points). It is more suited for representing models with internal edges (such as an hypercube).

Both support importing `.OBJ` models (even though `Polyhedron` is more naturally suited for this use-case).

`Sphere` is just a basic sphere.


## Usage

#### Basic

Importing a 3D model and displaying it.

```lua
local Polyhedron = include('lib/3d/polyhedron')
local draw_mode = include('lib/3d/enums/draw_mode')

local model = Polyhedron.new_from_obj("/home/we/dust/code/3d/model/teapot.obj")
local level = 15
model:draw(level, draw_mode.FACES)
```

Rotating it:

```lua
local axis = include('lib/3d/enums/axis')

model:rotate(axis.Y, 0.02)
```

Drawing can take a multiplication coefficient and a camera position:

```lua
local mult = 64        -- scale up model by 640%
local cam = {0, 0, -4} -- camera coordinates (x, y, z)
model:draw(level, draw_mode.FACES, mult, cam)
```

This is important as `.OBJ` models vary greatly in scale and are not necessarily origin-centered.

See the [teapot](./obj_teapot.lua) (`Polyhedron`) and [wireframe_cube](./wireframe_cube.lua) (`Wireframe`) examples for this basic use-case.


#### Drawing modes

Several draw mode are supported:

```lua
model:draw(nil,   draw_mode.FACES)     -- faces (not supported by `Wireframe`)
model:draw(level, draw_mode.WIREFRAME) -- edges
model:draw(level, draw_mode.POINTS)    -- vertices
```

And can be combined:

```lua
model:draw(level, draw_mode.FACES | draw_mode.WIREFRAME) -- faces + edges
```

In this case, independent screen levels can be specified:

```lua
model:draw(level, draw_mode.WIREFRAME | draw_mode.POINTS, nil, nil,
           {line_level = 10,
            point_level = 5})
```

See the [octagon](./obj_octagon.lua) example to illustrate this use-case.


#### Custom drawing function

A custom drawing function can be configured:

```lua
function draw_v_as_circle(x, y, l)
  if l then
    screen.level(l)
  end
  local radius = 2
  screen.move(x + radius, y)
  screen.circle(x, y, radius)
  screen.fill()
end

model:draw(level, draw_mode.POINTS, mult, cam,
           {point_draw_fn = draw_v_as_circle})
```

Custom drawing function parameter depends of `draw_mode`:

| object \ draw_mode | `POINTS`                 | `WIREFRAME`                        | `FACES`                    |
| ---                | ---                      | ---                                | ---                        |
| `Wireframe`        | `point_draw_fn(x, y, l)` | `lines_draw_fn(x0, y0, x1, y1, l)` | n/a                        |
| `Polyhedron`       | `point_draw_fn(x, y, l)` | `face_edges_draw_fn(f_edges, l)`   | `face_draw_fn(f_edges, l)` |


See the [octagon](./obj_octagon.lua) example to illustrate this use-case.


#### Conditional drawing

Drawing of vertices/edges/faces can be conditional thanks to these props:

| prop       | description                                            |
| ---        | ---                                                    |
| `draw_pct` | % of chance that element get drawn                     |
| `min_z`    | elements w/ at least 1 vertex bellow value are skipped |
| `maw_z`    | elements w/ at least 1 vertex above value are skipped |

When tuned appropriately, this can lead to a nice glitchy effect.

See the [octaglitch](./obj_octaglitch.lua) example.

<details><summary markdown="span"><b>!!! EPILEPSY WARNING !!!</b></summary>
<img src="https://www.eigenbahn.com/assets/gif/norns_3d_glitch.gif"/>
</details>


#### Glitchy elements

`Wireframe`, when in `draw_mode.WIREFRAME`, supports drawing random lines between vertices.

| prop                     | description                                      |
| ---                      | ---                                              |
| `glitch_edge_pct`        | % of chance that element get drawn               |
| `glitch_edge_amount_pct` | % of total vertices that attempts getting linked |

See the [glitchpercube](./obj_glitchpercube.lua) example.

<details><summary markdown="span"><b>!!! EPILEPSY WARNING !!!</b></summary>
<img src="https://www.eigenbahn.com/assets/gif/norns_3d_glitchpercube.gif"/>
</details>


## Limitations

No clean masking support, elements (faces / edges / vertices) are drawn in no specific order.

Basic masking could be enabled tuning the `min_z` drawing property, even though that'll only work properly for [highly symmetrical models](https://en.wikipedia.org/wiki/Polyhedron#Symmetries).

No support for *materials*.

Currently, glitches (conditional drawing, random elements) refresh at the same rate as the element is being drawn. Ideally we should split this "glicthing" logic from the drawing logic for it to be less aggressive.


## Acknowledgements

90% of the 3D vertex calculation code is based on an [example](https://gist.github.com/Ivoah/477775d13e142b2c89ba) by [@Ivoah](https://github.com/Ivoah) for [PICO-8](https://www.lexaloffle.com/pico-8.php).

It has been modified to rely on a mutating state for better performance and preventing memory consumption to grow out of control (I assume GC tuning is a bit conservative on norns).

Lowpoly 3D fish models used in `obj_fish.lua` example by [@rkuhlf](https://rkuhlf-assets.itch.io/) ([source](https://www.cgtrader.com/free-3d-models/animals/fish/low-poly-fish-b981402c-4bac-491b-a4d8-6bc91b8e08b0)).
