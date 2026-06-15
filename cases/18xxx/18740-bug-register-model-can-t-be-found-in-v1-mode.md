# vllm-project/vllm#18740: [Bug]: register model can't be found in v1 mode

| 字段 | 值 |
| --- | --- |
| Issue | [#18740](https://github.com/vllm-project/vllm/issues/18740) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: register model can't be found in v1 mode

### Issue 正文摘录

### model registry in vllm 0.8.5.post1 ### 🐛 Describe the bug there is a bug in vllm v1 mode, the detail i found is that vllm_config will be changed in vllm/v1/engine/core.py: def run_engine_core and vllm/v1/utils.py: self.proc: Process = context.Process(target=target_fn, , Theoretically, kwargs and process_kwargs should be identical, but in practice they differ. Specifically, the keys returned by kwargs.vllm_config.model_config.registry.models.keys() are missing the name of my custom-registered model. ![Image](https://github.com/user-attachments/assets/98efe76e-479d-4fc5-8053-213113f29c49) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: register model can't be found in v1 mode bug ### model registry in vllm 0.8.5.post1 ### 🐛 Describe the bug there is a bug in vllm v1 mode, the detail i found is that vllm_config will be changed in vllm/v1/engine/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and process_kwargs should be identical, but in practice they differ. Specifically, the keys returned by kwargs.vllm_config.model_config.registry.models.keys() are missing the name of my custom-registered model. ![Image]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 49) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
