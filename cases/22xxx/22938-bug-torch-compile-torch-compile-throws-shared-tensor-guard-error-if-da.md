# vllm-project/vllm#22938: [Bug] [torch.compile]: torch.compile throws shared tensor guard error if data attribute is accessed

| 字段 | 值 |
| --- | --- |
| Issue | [#22938](https://github.com/vllm-project/vllm/issues/22938) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [torch.compile]: torch.compile throws shared tensor guard error if data attribute is accessed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Context ### For more context, see https://github.com/vllm-project/vllm/issues/22937. TLDR, I'm trying to pass a model's data into a linear kernel. ### Bug Description ### Attempting to access the `data` attribute of a vllm parameter causes torch.compile to raise an error about duplicate tensors, despite there being no duplicate tensors in the model. This error does not get raised if the `data` attribute is accessed outside of the forward function, which leads me to thinking that this is either a torch.compile issue or related to a change to torch.compile done by vllm. https://github.com/vllm-project/vllm/compare/main...neuralmagic:vllm:kylesayrs/access-data ``` AssertionError: Guard check failed: 0/0: Duplicate tensors found: ["self._modules['layers']._modules['0']._modules['mlp']._modules['down_proj']._parameters['weight'].data", "self._modules['layers']._modules['1']._modules['mlp']._modules['down_proj']._parameters['weight'].data", "self._modules['layers']._modules['2']._modules['mlp']._modules['down_proj']._parameters['weight'].data","self._modules['layers']._modules['3']._modules['mlp']._modules['down_proj']._parameters[...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug] [torch.compile]: torch.compile throws shared tensor guard error if data attribute is accessed bug ### Your current environment ### 🐛 Describe the bug ### Context ### For more context, see https://github.com/vllm-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your curren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ://github.com/vllm-project/vllm/issues/22937. TLDR, I'm trying to pass a model's data into a linear kernel. ### Bug Description ### Attempting to access the `data` attribute of a vllm parameter causes torch.compile to r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
