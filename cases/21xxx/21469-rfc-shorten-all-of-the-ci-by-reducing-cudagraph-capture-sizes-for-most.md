# vllm-project/vllm#21469: [RFC]: Shorten all of the CI by reducing `cudagraph_capture_sizes` for most of the unit tests

| 字段 | 值 |
| --- | --- |
| Issue | [#21469](https://github.com/vllm-project/vllm/issues/21469) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Shorten all of the CI by reducing `cudagraph_capture_sizes` for most of the unit tests

### Issue 正文摘录

### Motivation. The CI is slow due to large number of graph length to capture. Many of the CI are using the default graph size which captures all 67 graph sizes. ``` "cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1] ``` As a low hanging fruit to reduce CI time. We can first reduce the number of graph capture size. Another reason that there is no need to capture all size is in the CI, the input batch size are generally very small. (Most of them are 1 or 2 input prompts) We still capture some graph size to ensure that the graph capturing logic is functional, and when invoking the graph during inferencing is also working as intended. ### Proposed Change. Proposal 1:. Introduce switches such as environment variable envs.MODE == "CI" which will set `cudagraph_capture_sizes` to fewer size to capture e.g. `[1,2,4,8]`. Only need to override `cudagraph_capture_sizes` at where `cudagraph_capture_sizes` is assigned. This envs.MODE can also be used to control other futu...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Shorten all of the CI by reducing `cudagraph_capture_sizes` for most of the unit tests RFC ### Motivation. The CI is slow due to large number of graph length to capture. Many of the CI are using the default graph...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Shorten all of the CI by reducing `cudagraph_capture_sizes` for most of the unit tests RFC ### Motivation. The CI is slow due to large number of graph length to capture. Many of the CI are using the default graph...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: all of the CI by reducing `cudagraph_capture_sizes` for most of the unit tests RFC ### Motivation. The CI is slow due to large number of graph length to capture. Many of the CI are using the default graph size which cap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
