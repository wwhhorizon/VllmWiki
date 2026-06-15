# vllm-project/vllm#42801: [Bug]: Significant accuracy discrepancies across different vLLM versions.

| 字段 | 值 |
| --- | --- |
| Issue | [#42801](https://github.com/vllm-project/vllm/issues/42801) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Significant accuracy discrepancies across different vLLM versions.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a substantial variance in DeepSeek R1's performance on the MMLU and HumanEval benchmarks when tested with different versions of vLLM. I evaluated the accuracy of DeepSeek R1 on the official MMLU and HumanEval datasets using the EvalScope framework with vLLM versions 0.10.2 and 0.20.2. The results are as follows: ``` vLLM 0.10.2: MMLU 0.9895, HumanEval 0.3633 vLLM 0.20.2: MMLU 0.9123(-0.077~), HumanEval 0.5165(+0.15~) ``` There is a noticeable performance regression for DeepSeek R1 on the latest vLLM release, with a clear drop in mmlu accuracy. I utilized the official weights and executed identical commands in both scenarios. The specific commands used to launch vLLM and evaluate the benchmark accuracy are provided below: ``` vllm serve /share_data/hf/DeepSeek-R1-FP8/ --tensor-parallel-size 8 --data-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 32768 --trust-remote-code --dtype bfloat16 --port 8080 --enable-expert-parallel python tools/evaluate/evalscope/run_evalscope.py --task humaneval --model-path /share_data/hf/DeepSeek-R1-FP8/ --server-port 8080 ``` Both test environments are running the same version o...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: accuracy are provided below: ``` vllm serve /share_data/hf/DeepSeek-R1-FP8/ --tensor-parallel-size 8 --data-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 32768 --trust-remote-code --dtype bfloat16 --port...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Significant accuracy discrepancies across different vLLM versions. bug ### Your current environment ### 🐛 Describe the bug There is a substantial variance in DeepSeek R1's performance on the MMLU and HumanEval be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Significant accuracy discrepancies across different vLLM versions. bug ### Your current environment ### 🐛 Describe the bug There is a substantial variance in DeepSeek R1's performance on the MMLU and HumanEval be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e the benchmark accuracy are provided below: ``` vllm serve /share_data/hf/DeepSeek-R1-FP8/ --tensor-parallel-size 8 --data-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 32768 --trust-remote-code --dtype...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: odel-len 32768 --trust-remote-code --dtype bfloat16 --port 8080 --enable-expert-parallel python tools/evaluate/evalscope/run_evalscope.py --task humaneval --model-path /share_data/hf/DeepSeek-R1-FP8/ --server-port 8080...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
