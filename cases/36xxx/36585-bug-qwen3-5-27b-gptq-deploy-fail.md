# vllm-project/vllm#36585: [Bug]: qwen3.5-27b-gptq deploy fail

| 字段 | 值 |
| --- | --- |
| Issue | [#36585](https://github.com/vllm-project/vllm/issues/36585) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3.5-27b-gptq deploy fail

### Issue 正文摘录

### Your current environment torch 2.10.0 torchaudio 2.10.0+cu128 torchvision 0.25.0+cu128 tqdm 4.67.3 transformers 4.57.6 vllm 0.17.0 GPTQModel 5.7.1 ### 🐛 Describe the bug after installing vllm0170, the transformers 4.57.6 version is automatically installed, and deploying this configuration using the official website qwen3-5-27b succeeds. However, when deploying the model fine-tuned by swift, a ValueError occurs: Tokenizer class TokenizersBackend does not exist or is not currently imported.The solution is also to "retain the model.safetensors.index.json and *.safetensors obtained after training, and use the original files for the rest" like:https://github.com/modelscope/ms-swift/issues/8098 After following this operation, the modified configuration can successfully launch the model after sft with vllm; however, when I use this configuration to quantize the sft model to int8 using gptq, this issue occurs: ``` Value error, The checkpoint you are trying to load has model type qwen3_5_text but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. You can update Transformers wi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: qwen3.5-27b-gptq deploy fail bug ### Your current environment torch 2.10.0 torchaudio 2.10.0+cu128 torchvision 0.25.0+cu128 tqdm
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: GPTQModel 5.7.1 ### 🐛 Describe the bug after installing vllm0170, the transformers 4.57.6 version is automatically installed, and deploying this configuration using the official website qwen3-5-27b succeeds. However, wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: he model after sft with vllm; however, when I use this configuration to quantize the sft model to int8 using gptq, this issue occurs: ``` Value error, The checkpoint you are trying to load has model type qwen3_5_text bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oad has model type qwen3_5_text but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. You can update Transf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel fine-tuned by swift, a ValueError occurs: Tokenizer class TokenizersBackend does not exist or is not currently imported.The solution is also to "retain the model.safetensors.index.json and *.safetensors obtained af...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
