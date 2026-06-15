# vllm-project/vllm#20283: [RFC][UX][torch.compile][CUDAGraph]: Overhaul `CompilationConfig` and improve CLI `-O<n>`

| 字段 | 值 |
| --- | --- |
| Issue | [#20283](https://github.com/vllm-project/vllm/issues/20283) |
| 状态 | closed |
| 标签 | RFC;torch.compile;keep-open;startup-ux |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][UX][torch.compile][CUDAGraph]: Overhaul `CompilationConfig` and improve CLI `-O<n>`

### Issue 正文摘录

**tl;dr**: Improve the user experience around compilation and cudagraph capture by consolidating/overhauling `CompilationConfig` and defining more meaningful optimization levels `-O0`, `-O1`, `-O2`, `-O3` (and maybe more). ## Motivation. `CompilationConfig` was born around December 2024 to enable configuring `torch.compile`-based compilation and piecewise cudagraph capture. Since then, a bunch more flags were added to support new features, all good in isolation but without a cohesive plan. As vLLM aims to provide great performance out-of-the-box, having to manually configure a bunch of flags is bad UX. `CompilationConfig` currently serves as both the user-facing and compiler-interfacing compilation configuration mechanism. What I mean by that is that it's used by CLI/Python API users to control compilation, as well as other parts of the codebase (model runner, vllm config, etc.). This has the benefit of good UX for developers to directly control compilation from the CLI and Python, but the downside of this weird second-state where defaults are inspected and adjusted. This was handled very poorly in V1 where a bunch of settings were hardcoded, making them impossible to change from...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC][UX][torch.compile][CUDAGraph]: Overhaul `CompilationConfig` and improve CLI `-O<n>` RFC;torch.compile;keep-open;startup-ux **tl;dr**: Improve the user experience around compilation and cudagraph capture by consoli...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC][UX][torch.compile][CUDAGraph]: Overhaul `CompilationConfig` and improve CLI `-O<n>` RFC;torch.compile;keep-open;startup-ux **tl;dr**: Improve the user experience around compilation and cudagraph capture by consoli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC][UX][torch.compile][CUDAGraph]: Overhaul `CompilationConfig` and improve CLI `-O<n>` RFC;torch.compile;keep-open;startup-ux **tl;dr**: Improve the user experience around compilation and cudagraph capture by consoli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rmance. We can decide exact settings for each levels after more in-depth benchmarking as proposed in #19824. While we should make sure each level is just a combination of fine-grained flags, I also believe we should not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nge, 🌱 means addition - ❌ `use_inductor`: this is fully redundant with `backend` - ✏ `backend`: this is currently not respected for compilation mode (level) 3 (PIECEWISE), and use_inductor is used in its place. We can i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
