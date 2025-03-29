import { EleventyHtmlBasePlugin, IdAttributePlugin } from "@11ty/eleventy";
import markdownIt from "markdown-it";
import { DateTime } from "luxon";
import { execSync } from "child_process";
import implicitFigures from "markdown-it-implicit-figures";
import memoize from "memoize";

export const META = {
  APPLE_TOUCH_ICON: "apple-touch-icon.png",
  BUILD_TIME: new Date().toISOString(),
  CANONICAL: "https://norns.community",
  DAUNTLESS_CHOIR_URL: "/dauntless-choir/",
  DESCRIPTION: "a script index for the monome norns sound computer",
  FAVICON: "favicon.ico",
  GIT_HASH_SHORT: execSync("git rev-parse --short HEAD").toString().trim(),
  GIT_HASH: execSync("git rev-parse HEAD").toString().trim(),
  GITHUB_URL: "https://github.com/monome-community/norns-community",
  TITLE: "norns-community",
  YEAR: new Date().getUTCFullYear(),
};

export const DIRS = {
  DATA: "data",
  IMAGES: "images",
  INCLUDES: "includes",
  INPUT: "src",
  LAYOUTS: "layouts",
  OUTPUT: "dist",
  PAGES: "pages",
  POSTS: "posts",
};

export default async (eleventyConfig) => {
  eleventyConfig.addGlobalData("eleventyComputed.permalink", (data) => {
    if (!data?.page || !data?.page.inputPath) {
      return false;
    }

    if (data.page.inputPath.includes("/tags/")) {
      return `/tags/${data.page.fileSlug}/index.html`;
    } else if (data.page.inputPath.includes("/projects/")) {
      return `/projects/${data.page.fileSlug}/index.html`;
    }
    return `/${data.page.fileSlug}/index.html`;
  });

  const markdownLib = markdownIt({ html: true }).use(implicitFigures, {
    figcaption: false,
  });

  // eleventyConfig.setLibrary("md", markdownLib);

  // eleventyConfig.addFilter(
  //   "markdown",
  //   memoize((content) => {
  //     return markdownLib.render(content);
  //   })
  // );

  // eleventyConfig.addPlugin(IdAttributePlugin);

  // eleventyConfig.addPlugin(EleventyHtmlBasePlugin, {
  //   extensions: "html,md,scss",
  // });

  // eleventyConfig.addPassthroughCopy(`${DIRS.INPUT}/${META.FAVICON}`);
  // eleventyConfig.addPassthroughCopy(`${DIRS.INPUT}/${META.APPLE_TOUCH_ICON}`);
  // eleventyConfig.addPassthroughCopy(`${DIRS.INPUT}/${META.LOGO}`);
  // eleventyConfig.addPassthroughCopy(`${DIRS.INPUT}/${DIRS.IMAGES}`);
  // eleventyConfig.addPassthroughCopy(`${DIRS.INPUT}/${DIRS.FONTS}`);

  // eleventyConfig.setLiquidOptions({
  //   jsTruthy: true,
  //   dynamicPartials: false,
  // });

  return {
    markdownTemplateEngine: "liquid",
    dir: {
      input: DIRS.INPUT,
      data: DIRS.DATA,
      includes: DIRS.INCLUDES,
      layouts: DIRS.LAYOUTS,
      output: DIRS.OUTPUT,
    },
  };
};
