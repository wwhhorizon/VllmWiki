# vllm-project/vllm#28301: [Performance]: DeepSeek V3 performance drop when enabling MTP on both H200 and MI300X

| 字段 | 值 |
| --- | --- |
| Issue | [#28301](https://github.com/vllm-project/vllm/issues/28301) |
| 状态 | closed |
| 标签 | performance;rocm;speculative-decoding;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: DeepSeek V3 performance drop when enabling MTP on both H200 and MI300X

### Issue 正文摘录

### Proposal to improve performance Hi all, I'm testing the MTP feature in vLLM. I enabled MTP for DeepSeek V3 serving running on both NVIDIA H200s and AMD MI300Xs and found that there is a performance drop when enabling MTP on both platforms. The detailed instructions for reproducing the findings can be referred as below. For NVIDIA H200: Docker image: vllm/vllm-openai:latest (2025/10/28) The command for launching the server: `vllm serve /models/DeepSeek-V3/ --tensor-parallel-size 8 --max-model-len 65536 --max-num-seqs 1024 --max-num-batched-tokens 32768 --disable-log-requests --block-size 1 --compilation-config '{"full_cuda_graph":false,"cudagraph_mode":"PIECEWISE"}' --trust-remote-code --speculative_config '{"model": "/models/DeepSeek-V3-NextN/", "num_speculative_tokens": 2}'` For MI300X: Docker image: rocm/vllm:latest The command for launching the server: `export VLLM_ATTENTION_BACKEND=ROCM_AITER_MLA vllm serve /models/DeepSeek-V3/ --tensor-parallel-size 8 --max-model-len 65536 --max-num-seqs 512 --max-num-batched-tokens 32768 --disable-log-requests --port 8001 --block-size 1 --compilation-config '{"full_cuda_graph":false,"cudagraph_mode":"PIECEWISE"}' --trust-remote-code --sp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rmance]: DeepSeek V3 performance drop when enabling MTP on both H200 and MI300X performance;rocm;speculative-decoding;stale ### Proposal to improve performance Hi all, I'm testing the MTP feature in vLLM. I enabled MTP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: formance drop when enabling MTP on both H200 and MI300X performance;rocm;speculative-decoding;stale ### Proposal to improve performance Hi all, I'm testing the MTP feature in vLLM. I enabled MTP for DeepSeek V3 serving...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: culative-decoding;stale ### Proposal to improve performance Hi all, I'm testing the MTP feature in vLLM. I enabled MTP for DeepSeek V3 serving running on both NVIDIA H200s and AMD MI300Xs and found that there is a perfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llm:latest The command for launching the server: `export VLLM_ATTENTION_BACKEND=ROCM_AITER_MLA vllm serve /models/DeepSeek-V3/ --tensor-parallel-size 8 --max-model-len 65536 --max-num-seqs 512 --max-num-batched-tokens 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hen enabling MTP on both platforms. The detailed instructions for reproducing the findings can be referred as below. For NVIDIA H200: Docker image: vllm/vllm-openai:latest (2025/10/28) The command for launching the serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
