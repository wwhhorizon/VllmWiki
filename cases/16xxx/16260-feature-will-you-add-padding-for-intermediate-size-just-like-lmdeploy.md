# vllm-project/vllm#16260: [Feature]: Will you add padding for intermediate_size just like lmdeploy?

| 字段 | 值 |
| --- | --- |
| Issue | [#16260](https://github.com/vllm-project/vllm/issues/16260) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Will you add padding for intermediate_size just like lmdeploy?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I use awq model like InternVL2-5-78B-AWQ, for example(on A100) vllm serve /path/to/vlm/InternVL2_5-78B-AWQ/ --port xxxxx --trust-remote-code --tensor-parallel-size 4 --quantization=awq --dtype float16 It will raise a ValueError like this: ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. As I know, the reason is intermediate_size(29568 for internvl25-78b-awq) % (quant_group_size(128) * tp(4)) != 0. There are codes which raise the error: ![Image](https://github.com/user-attachments/assets/dcfd8c0a-ab4e-43a0-a29f-f658b0a07e18) However, when i use lmdeploy to serve the same model with same devices and parameters, it works. When reading lmdeploy's src i found they do sth like this: ![Image](https://github.com/user-attachments/assets/e5f73fb3-15cd-4b2a-8448-7f6e3f399ac7) So they always make intermediate_size% (quant_group_size * tp) == 0 I tried to add the padding feature to vllm's src, concat zero parameters to the loaded_weights and change the quant_weight to make the model can be loaded. But the model cannot pass the dummy_input. The matmul dimensions are not t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: re request;stale ### 🚀 The feature, motivation and pitch When I use awq model like InternVL2-5-78B-AWQ, for example(on A100) vllm serve /path/to/vlm/InternVL2_5-78B-AWQ/ --port xxxxx --trust-remote-code --tensor-paralle...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 2_5-78B-AWQ/ --port xxxxx --trust-remote-code --tensor-parallel-size 4 --quantization=awq --dtype float16 It will raise a ValueError like this: ValueError: The input size is not aligned with the quantized weight shape....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and pitch When I use awq model like InternVL2-5-78B-AWQ, for example(on A100) vllm serve /path/to/vlm/InternVL2_5-78B-AWQ/ --port xxxxx --trust-remote-code --tensor-parallel-size 4 --quantization=awq --dtype float16 It...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Will you add padding for intermediate_size just like lmdeploy? feature request;stale ### 🚀 The feature, motivation and pitch When I use awq model like InternVL2-5-78B-AWQ, for example(on A100) vllm serve /path/to/vlm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: requently asked questions. development distributed_parallel;frontend_api;gemm_linear;model_support;multimodal_vlm;quantization cuda;gemm;quantization dtype;shape 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
