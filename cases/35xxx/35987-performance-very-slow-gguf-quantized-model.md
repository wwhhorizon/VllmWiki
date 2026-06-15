# vllm-project/vllm#35987: [Performance]: Very slow GGUF quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#35987](https://github.com/vllm-project/vllm/issues/35987) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Very slow GGUF quantized model

### Issue 正文摘录

### Proposal to improve performance Hi, I was testing a GGUF quantized model (sarvam-m) and surprisingly it's considerably slower than its non-quantized counterpart. Specifically the TTFT is very high (below are some results). Do you have any explanation for this? Thanks! ## Benchmark used ```bash vllm bench serve --model sarvamai/sarvam-m --dataset-name random --base-url http://127.0.0.1:8090 --max-concurrency 5 --random-input-len 100 --num-prompts 50 --request-rate 5 ``` ## sarvamai/sarvam-m (https://huggingface.co/sarvamai/sarvam-m/tree/main) ```bash ---------------Time to First Token---------------- Mean TTFT (ms): 116.94 Median TTFT (ms): 114.55 P99 TTFT (ms): 150.41 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 36.29 Median TPOT (ms): 36.26 P99 TPOT (ms): 36.73 ---------------Inter-token Latency---------------- Mean ITL (ms): 37.28 Median ITL (ms): 35.92 P99 ITL (ms): 80.92 ============================================== ``` ## sarvamai/sarvam-m-q8-gguf (https://huggingface.co/sarvamai/sarvam-m-q8-gguf) ```bash ---------------Time to First Token---------------- Mean TTFT (ms): 4140.51 Median TTFT (ms): 4928.44 P99 TTFT (ms): 4940.83 -----Time per Output T...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: risingly it's considerably slower than its non-quantized counterpart. Specifically the TTFT is very high (below are some results). Do you have any explanation for this? Thanks! ## Benchmark used ```bash vllm bench serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ntized model performance ### Proposal to improve performance Hi, I was testing a GGUF quantized model (sarvam-m) and surprisingly it's considerably slower than its non-quantized counterpart. Specifically the TTFT is ver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Very slow GGUF quantized model performance ### Proposal to improve performance Hi, I was testing a GGUF quantized model (sarvam-m) and surprisingly it's considerably slower than its non-quantized counterp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
