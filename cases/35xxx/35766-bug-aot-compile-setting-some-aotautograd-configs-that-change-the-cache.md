# vllm-project/vllm#35766: [Bug]: aot_compile setting some aotautograd configs that change the cache key

| 字段 | 值 |
| --- | --- |
| Issue | [#35766](https://github.com/vllm-project/vllm/issues/35766) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: aot_compile setting some aotautograd configs that change the cache key

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug some output from claude: ``` Here's the summary of the root cause and fix: Root Cause When VLLM_USE_AOT_COMPILE is enabled (which is the default on torch >= 2.10), the compilation path goes through aot_compile_fullgraph() in torch._dynamo.aot_compile. This function patches two torch._functorch.config values: - strict_autograd_cache = True - force_non_lazy_backward_lowering = True These patches are applied as a context manager around the backend call (VllmBackend.__call__). Before this commit (lazy compilation): compile_all_ranges() didn't exist; compilation happened lazily during execution, after VllmBackend.__call__ returned and the aot_compile_fullgraph context manager had exited. So these patched values were not active when the autograd cache key was computed. After this commit (eager compilation): compile_all_ranges() runs inside VllmBackend.__call__, while the aot_compile_fullgraph patches are still active. The autograd cache key captures strict_autograd_cache=True and force_non_lazy_backward_lowering=True. During warm start, the non-unique subgraphs go through standalone_compile() which does NOT apply these patches, so...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: aot_compile setting some aotautograd configs that change the cache key bug;torch.compile ### Your current environment main ### 🐛 Describe the bug some output from claude: ``` Here's the summary of the root cause...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: wering = True These patches are applied as a context manager around the backend call (VllmBackend.__call__). Before this commit (lazy compilation): compile_all_ranges() didn't exist; compilation happened lazily during e...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: hese patches, so their autograd cache key has False for both — causing a cache miss. Fix Explicitly reset these two configs to False inside compile_all_ranges() (alongside the existing bundled_autograd_cache=True patch)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: () which does NOT apply these patches, so their autograd cache key has False for both — causing a cache miss. Fix Explicitly reset these two configs to False inside compile_all_ranges() (alongside the existing bundled_a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
