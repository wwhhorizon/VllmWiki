# vllm-project/vllm#10674: [RFC]: Make any vLLM model a pooling model

| 字段 | 值 |
| --- | --- |
| Issue | [#10674](https://github.com/vllm-project/vllm/issues/10674) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Make any vLLM model a pooling model

### Issue 正文摘录

### Motivation. Currently, we have to open new PRs to add pooling functionality for existing architectures supported in vLLM. Since the code involved is basically the same for each model, there is potential to automate away this boilerplate. ### Proposed Change. Implement a pooling adapter that can be applied to any existing text generation model in vLLM. To preserve features such as LoRA, PP and multimodality, the adapter simply creates a new subclass of the original model. - [x] Embedding model adapter: #10769 - [ ] Classification model adapter #11469 - [ ] Reward model adapter #11469 The pooling adapter to apply depends on the purpose of the model. To facilitate this, the `embedding` task will be split up, so that the user can specify which adapter to apply to the model via `--task`: - [x] #10820 - [x] #11457 Meanwhile, current embedding-related classes will be renamed to avoid confusion between `embed` and other pooling tasks: - [x] #10801 ### Feedback Period. 1-2 weeks ### CC List. @youkaichao @mgoin @robertgshaw2-neuralmagic @maxdebayser ### Any Other Things. Note that we can still directly map to pooling models in the model registry. This is used when the model architecture...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Make any vLLM model a pooling model RFC ### Motivation. Currently, we have to open new PRs to add pooling functionality for existing architectures supported in vLLM. Since the code involved is basically the same...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: The pooling adapter to apply depends on the purpose of the model. To facilitate this, the `embedding` task will be split up, so that the user can specify which adapter to apply to the model via `--task`: - [x] #10820 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ently, we have to open new PRs to add pooling functionality for existing architectures supported in vLLM. Since the code involved is basically the same for each model, there is potential to automate away this boilerplat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
