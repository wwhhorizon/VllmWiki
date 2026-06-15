# vllm-project/vllm#7031: [Bug]: Llama 3.1 405 B FP8 model is not support by vLLM (v0.5.3.post1) on AMD GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#7031](https://github.com/vllm-project/vllm/issues/7031) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 3.1 405 B FP8 model is not support by vLLM (v0.5.3.post1) on AMD GPU

### Issue 正文摘录

### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 AMD MI300x GPU ### 🐛 Describe the bug ![Screenshot 2024-07-31 131408](https://github.com/user-attachments/assets/5b0771b4-8b4b-4303-9eff-df8b425aaf60) vLLM is throwing value error when loading meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 on AMD MI300x GPU. Value Erorr: fbgemm_fp8 quantization is currently not supported in ROCm. Refer screenshot for reference.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Llama 3.1 405 B FP8 model is not support by vLLM (v0.5.3.post1) on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 AMD MI300x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 3.1 405 B FP8 model is not support by vLLM (v0.5.3.post1) on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 AMD MI300x GPU ### 🐛 Des...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama 3.1 405 B FP8 model is not support by vLLM (v0.5.3.post1) on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 AMD MI300x...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LM (v0.5.3.post1) on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 AMD MI300x GPU ### 🐛 Describe the bug ![Screenshot 2024-07-31 13...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: llama/Meta-Llama-3.1-405B-Instruct-FP8 on AMD MI300x GPU. Value Erorr: fbgemm_fp8 quantization is currently not supported in ROCm. Refer screenshot for reference. development hardware_porting;model_support;quantization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
