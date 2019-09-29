# Groupby and applying

https://towardsdatascience.com/how-to-use-the-split-apply-combine-strategy-in-pandas-groupby-29e0eb44b62e

We split the groups transiently and loop them over via an optimized Pandas inner code. We then **pass each group to** a specified function as either a `Series` or a `DataFrame` object

![img](https://miro.medium.com/max/1600/0*pg5iUGsYPVFNpixe)



The custom function should have one input parameter which will be either a `Series` or a `DataFrame` object, depending on whether a single or multiple columns are specified via the `groupby` method: