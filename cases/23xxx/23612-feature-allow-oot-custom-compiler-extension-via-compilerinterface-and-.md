# vllm-project/vllm#23612: [Feature]: Allow oot custom compiler extension via CompilerInterface and reuse backend-agnostic FX passes

| 字段 | 值 |
| --- | --- |
| Issue | [#23612](https://github.com/vllm-project/vllm/issues/23612) |
| 状态 | closed |
| 标签 | feature request;torch.compile |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow oot custom compiler extension via CompilerInterface and reuse backend-agnostic FX passes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From vllm-ascend, we are trying to enable some graph fusion passes by extending the vllm core. But it seems that the compilation backend is currently coupled with the "inductor" backend which not every HW backend supports. In vllm-ascend, the inductor backend is not yet enabled and we are adding direct FX-based graph fusion. Currently, we have to do monkey-patches to plugin our own passes (see the rmsnorm+quant fusion PR from @ganyi1996ppo: https://github.com/vllm-project/vllm-ascend/pull/2389). We also want to reuse the existing backend-agnostic FX passes from vllm core, e.g., sequence parallel fusion. But these are all "inductor" passes. In summary, it would be great if A HW backend can extend vllm to support custom compiler backend that implements CompilerInterface. A HW backend with custom compiler backend can reuse existing backend-agnostic FX passes.. Would love to get your inputs. PS: For "2", we can manually apply the AotDispatch passes and invoke those vllm "inductor" passes from inside the custom compiler backend. Not sure if that would work well though. Discussion context from: https://github.com/vllm-project/vllm/pull/23332#issue...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: re]: Allow oot custom compiler extension via CompilerInterface and reuse backend-agnostic FX passes feature request;torch.compile ### 🚀 The feature, motivation and pitch From vllm-ascend, we are trying to enable some gr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Allow oot custom compiler extension via CompilerInterface and reuse backend-agnostic FX passes feature request;torch.compile ### 🚀 The feature, motivation and pitch From vllm-ascend, we are trying to enable s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: posal We propose to add an extra field `oot_compiler` to the `CompilationConfig` for out-of-tree extension to plug in their own piece-wise compiler. Then, `make_compiler` is updated to check and load the `oot_compiler`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , we have to do monkey-patches to plugin our own passes (see the rmsnorm+quant fusion PR from @ganyi1996ppo: https://github.com/vllm-project/vllm-ascend/pull/2389). We also want to reuse the existing backend-agnostic FX...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
