# vllm-project/vllm#31368: [Performance]: DeepSeek-v3.2 throughput&TTFT&TPOT is much slower than DeepSeek-v3.1 on 8*H200

| 字段 | 值 |
| --- | --- |
| Issue | [#31368](https://github.com/vllm-project/vllm/issues/31368) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-v3.2 throughput&TTFT&TPOT is much slower than DeepSeek-v3.1 on 8*H200

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression ## Test Plan: ### DeepSeek-V3.1: ``` #!/bin/bash MODEL="/scratch-space/models/DeepSeek-V3.1" RESULTS_DIR="./benchmark_results" mkdir -p $RESULTS_DIR INPUT_LENS=(256 1024 2048 4096 8192 12288 16384) OUTPUT_LENS=(1024) REQUEST_RATE=(1 4 8 16) vllm serve $MODEL \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 8 \ --swap-space 16 \ --gpu-memory-utilization 0.9 & SERVER_PID=$! echo "Waiting for vLLM server to start..." while ! curl -s localhost:8000/health > /dev/null; do sleep 1 done echo "Server is ready!" for input_len in "${INPUT_LENS[@]}"; do for output_len in "${OUTPUT_LENS[@]}"; do for request_rate in "${REQUEST_RATE[@]}"; do echo "Test: input_len=$input_len, output_len=$output_len, request_rate=$request_rate" result_file="${RESULTS_DIR}/deepseek_v3.1_input${input_len}_output${output_len}_request_rate${request_rate}.json" vllm bench serve \ --backend vllm \ --model $MODEL \ --host localhost \ --port 8000 \ --dataset-name random \ --random-input-len $input_len \ --random-output-len $output_len \ --request-rate $request_rate \ --num-prompts 100 \ --save-result \ --result-dir $RESULTS_DIR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: DeepSeek-v3.2 throughput&TTFT&TPOT is much slower than DeepSeek-v3.1 on 8*H200 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression ## Test Plan: ### De...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: .json" vllm bench serve \ --backend vllm \ --model $MODEL \ --host localhost \ --port 8000 \ --dataset-name random \ --random-input-len $input_len \ --r
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mance regression ## Test Plan: ### DeepSeek-V3.1: ``` #!/bin/bash MODEL="/scratch-space/models/DeepSeek-V3.1" RESULTS_DIR="./benchmark_results" mkdir -p $RESULTS_DIR INPUT_LENS=(256 1024 2048 4096 8192 12288 16384) OUTP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
