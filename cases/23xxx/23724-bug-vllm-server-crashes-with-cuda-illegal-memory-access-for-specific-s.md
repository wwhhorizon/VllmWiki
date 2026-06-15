# vllm-project/vllm#23724: [Bug]: vLLM server crashes with CUDA illegal memory access for specific sequence lengths on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#23724](https://github.com/vllm-project/vllm/issues/23724) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM server crashes with CUDA illegal memory access for specific sequence lengths on B200

### Issue 正文摘录

Log files: [Archive.zip](https://github.com/user-attachments/files/22003970/Archive.zip) The vLLM server **launches successfully and initially responds to requests**, but crashes with **CUDA illegal memory access** and **ProcessGroupNCCL failures** after running for some time when using MXFP4 precision with FlashInfer attention backend on NVIDIA B200 GPUs. The crashes occur with specific **sequence-length and request-rate combinations** - identical server configurations work fine with certain parameters but crash catastrophically with others after a period of normal operation. ## Environment Details Base docker image: https://hub.docker.com/layers/vllm/vllm-openai/gptoss/images/sha256-23c3feefba723be97ff9e9bd769aed7d165839a79bc042eb8f3a13dd2a469e1c - **vLLM Version**: 0.10.1.1 - **PyTorch Version**: 2.7.1+cu128 - **NCCL Version**: 2.27.5+cuda12.8 - **CUDA Version**: 12.8 - **Driver Version**: 575.57.08 - **GPU**: 8 x NVIDIA B200 (Amazon EC2 P6-B200) ## Environment Variables The following environment variables were set (matching the [vLLM B200 MXFP4 recipe](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#b200)): ```bash export VLLM_ATTENTION_BACKEND=FLASHINFER e...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: vLLM server crashes with CUDA illegal memory access for specific sequence lengths on B200 bug;stale;gpt-oss Log files: [Archive.zip](https://github.com/user-attachments/files/22003970/Archive.zip) The vLLM server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: vLLM server crashes with CUDA illegal memory access for specific sequence lengths on B200 bug;stale;gpt-oss Log files: [Archive.zip](https://github.com/user-attachments/files/22003970/Archive.zip) The vLLM server...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ith CUDA illegal memory access for specific sequence lengths on B200 bug;stale;gpt-oss Log files: [Archive.zip](https://github.com/user-attachments/files/22003970/Archive.zip) The vLLM server **launches successfully and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: the [vLLM B200 MXFP4 recipe](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#b200)): ```bash export VLLM_ATTENTION_BACKEND=FLASHINFER export VLLM_USE_TRTLLM_ATTENTION=1 export VLLM_USE_TRTLLM_DECODE_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: L failures** after running for some time when using MXFP4 precision with FlashInfer attention backend on NVIDIA B200 GPUs. The crashes occur with specific **sequence-length and request-rate combinations** - identical se...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x762d928dc253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x762d92c94ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown f… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x762d272f8fdd in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x762d928dc253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unkn… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23730: Should have ROCm label: NO (0 matches) #23724: Should have ROCm label: NO (0 matches) #23720: Should have ROCm label: NO (0 matches) #23719: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
