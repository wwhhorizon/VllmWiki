# vllm-project/vllm#22937: [Bug] [torch.compile]: torch linear type error with BasevLLMParameter

| 字段 | 值 |
| --- | --- |
| Issue | [#22937](https://github.com/vllm-project/vllm/issues/22937) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [torch.compile]: torch linear type error with BasevLLMParameter

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Context ### I am trying to support weight_loader_v2 for unquantized parameters (as a part of trying to support transforms for compressed-tensors). This requires that all parameters are subclasses of `BasevLLMParameter`. However, attempting to convert the unquantized weight parameter leads to an error. ### Bug Description ### In summary, torch.compile will not recognize `ModelWeightParameter` as being a valid input type for `torch.nn.functional.linear`, which only accepts `torch.Tensors`. This does not seem to be an issue for other kernels, as they are custom ops with perhaps looser/no type enforcement from torch.compile. The associated changes can be found here. https://github.com/vllm-project/vllm/compare/main...neuralmagic:vllm:kylesayrs/unquatnized-vllmparam ``` torch._dynamo.exc.Unsupported: All __torch_function__ overrides for call TorchInGraphFunctionVariable( , nonstrict_traceable=False) with args [TensorVariable(), UserDefinedObjectVariable(ModelWeightParameter), ConstantVariable(NoneType: None)] and kwargs {} returned NotImplemented from user code: File "/home/kyle/vllm/vllm/model_executor/models/llama.py", line 385,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug] [torch.compile]: torch linear type error with BasevLLMParameter bug ### Your current environment ### 🐛 Describe the bug ### Context ### I am trying to support weight_loader_v2 for unquantized parameters (as a part...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: . ### Bug Description ### In summary, torch.compile will not recognize `ModelWeightParameter` as being a valid input type for `torch.nn.functional.linear`, which only accepts `torch.Tensors`. This does not seem to be an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llm/vllm/model_executor/layers/linear.py", line 230, in apply return dispatch_unquantized_gemm()(layer, x, layer.weight, bias) File "/home/kyle/vllm/vllm/model_executor/layers/utils.py", line 92, in default_unquantized_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e the bug ### Context ### I am trying to support weight_loader_v2 for unquantized parameters (as a part of trying to support transforms for compressed-tensors). This requires that all parameters are subclasses of `Basev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
