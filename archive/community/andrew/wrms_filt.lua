--[[

 ▄▀▀▀█▄    ▄▀▀█▀▄   ▄▀▀▀▀▄     ▄▀▀▀█▀▀▄ 
█  ▄▀  ▀▄ █   █  █ █    █     █    █  ▐ 
▐ █▄▄▄▄   ▐   █  ▐ ▐    █     ▐   █     
 █    ▐       █        █         █      
 █         ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▄▄▀ ▄▀       
█         █       █  █        █         

hi! how are you ?

glad you decided to stop in and check out this wrms mod

anyway this one really simple it's a great intro to the whole process

it adds 1 page that filters up wrm 1
since wrm 1 feeds back by default, u get some nice analog-delay-esque filter feedback tails. yum !

go ahead and read on, but if ya want some more info on the whole system check out wrms/wrms.lua

]]---

wrms = include "wrms/wrms" -- this one litile line is how we link in the rest of the wrms ecosystem

wrms.pages[#wrms.pages + 1] = { -- this part is important - we're adding a table to the end of a table in wrms that holds all the pages
                                -- to do that we get the table length (# operator), and index the next thing
                                
  label = "f", -- this is the name of the page as it appears to the right
  e2 = { -- we add a table here as enocoder 2 for controlling the filter cutoff 
    worm = 1, -- accepts 1, 2 or "both", essentially it just detirmines where the control appears on-screen
    label = "f", -- label for the control
    value = 1.0, -- initally the default value, but it also stores the live value for retrieval
    range = { 0.0, 1.0 }, -- the range of the value
    event = function(self, v) -- event() is called every time the value is changed, its job is to communicate with supercut and keep other values up-to-date
      supercut.post_filter_fc(1, util.linexp(0, 1, 1, 12000, v)) -- now we're changing the cutoff ! we use v as the current value from function args
                                                                -- & put it through some exponential scaling then pass it to post_filter_fc for wrm 1
    end
  },
  e3 = { -- wrm 1 filter resonance - similar deal, just with q
    worm = 1,
    label = "q",
    value = 0.3,
    range = { 0.0, 1.0 },
    event = function(self, v) 
      softcut.post_filter_rq(1,1 - v)
      softcut.post_filter_rq(2,1 - v)
    end
  },
  k2 = { -- wrm 1 filter on/off
    worm = 1,
    label = "filt",
    behavior = "toggle", -- keys have multiple behaviors. this time we're working with "toggle" which is an on/off control
    value = 0, -- value here moves between 0 & 1
    event = function(self, v, t) 
      if v == 0 then -- the default 0 lets the dry signal through and mutes the filter outputs
        supercut.post_filter_dry(1, 1)
        supercut.post_filter_lp(1, 0)
        supercut.post_filter_bp(1, 0)
        supercut.post_filter_hp(1, 0)
      elseif v == 1 then
        wrms.update_control(wrms.page_from_label("f").k3) -- if value is 1 we'll update the next control, which sets filter type when fitler is toggled on
      end
    end
  },
  k3 = { -- wrm 1 filter type
    worm = 1,
    behavior = "enum", -- enum (enumerator) is a list of values that a key will step through
    label = { "lp", "bp", "hp"  }, -- the list of options is stored in the label field
    value = 1,
    event = function(self, v, t)
      if wrms.page_from_label("f").k2.value == 1 then -- first we'll check if the filter is on before changing settings
        supercut.post_filter_dry(1, 0) -- start by zeroing dry and all filter types
        supercut.post_filter_lp(1, 0)
        supercut.post_filter_bp(1, 0)
        supercut.post_filter_hp(1, 0)
        
        -- then based on the option, we'll crank the output of a filter up to 1
        
        if v == 1 then -- v is lowpass
          supercut.post_filter_lp(1, 1)
        elseif v == 2 then -- v is bandpass
          supercut.post_filter_bp(1, 1)
        elseif v == 3 then -- v is hightpass
          supercut.post_filter_hp(1, 1)
        end
      end
    end
  }
}