# vllm-project/vllm#26659: [Performance]:  Comparing MoE Model Quantization Performance on Different Inference Engines.

| 字段 | 值 |
| --- | --- |
| Issue | [#26659](https://github.com/vllm-project/vllm/issues/26659) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:  Comparing MoE Model Quantization Performance on Different Inference Engines.

### Issue 正文摘录

### Proposal to improve performance We noticed that the website https://inferencemax.semianalysis.com/ compares the performance of numerous models across different inference engines. Checking the GitHub deployment script at https://github.com/InferenceMAX/InferenceMAX, we see that while all models are compared using TRT, some use SGL, and others use vLLM. We suspect that vLLM's performance for deploying FP4 precision models on Blackwell-architecture GPUs may be worse than SGL's. Hence, we want to compare how different precision models perform under various deployment strategies, on different inference engines, and running on different GPU types. This issue is mainly for tracking these comparisons. ## **Deployment Scripts for Different Inference Engines** | Hardware | Precision | Inference Engine | Status | Script Name | | :--- | :--- | :--- | :--- | :--- | | **B200** | **FP4** | SGLang | Exists | `dsr1_fp4_b200_docker.sh` | | | | TRT-LLM | Exists | `dsr1_fp4_b200_trt_slurm.sh` | | | | vLLM | Missing (Completed) | `dsr1_fp4_b200_vllm_slurm.sh` | | | **FP8** | SGLang | Exists | `dsr1_fp8_b200_docker.sh` | | | | TRT-LLM | Exists | `dsr1_fp8_b200_trt_slurm.sh` | | | | vLLM | Missing (...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Comparing MoE Model Quantization Performance on Different Inference Engines. performance ### Proposal to improve performance We noticed that the website https://inferencemax.semianalysis.com/ compares the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: others use vLLM. We suspect that vLLM's performance for deploying FP4 precision models on Blackwell-architecture GPUs may be worse than SGL's. Hence, we want to compare how different precision models perform under vario...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: We suspect that vLLM's performance for deploying FP4 precision models on Blackwell-architecture GPUs may be worse than SGL's. Hence, we want to compare how different precision models perform under various deployment str...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Comparing MoE Model Quantization Performance on Different Inference Engines. performance ### Proposal to improve performance We noticed that the website https://inferencemax.semianalysis.com/ compares the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: determine the optimal PD separation strategy. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
