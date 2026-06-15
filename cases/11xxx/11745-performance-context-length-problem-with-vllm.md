# vllm-project/vllm#11745: [Performance]: Context Length Problem with VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#11745](https://github.com/vllm-project/vllm/issues/11745) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Context Length Problem with VLLM

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi guys, I was using my home server(2x 2080Ti 22g + 1x Tesla P4 8g, total of 52gb Vram) for selfhosted API usage. And now I'm confused while switch from ollama to vllm. My sys is ubuntu 20.04 LTS. I was using ollama serving qwen2.5:32b-instruct_q4_K_M for couple of months. Set num_ctx to more than 32k for processing transcription of meetings. I tested when context set to 39000, it took around 44gb of vram. The problem comes when I tried to switch to vllm (docker, allocated the 2 2080ti gpus and available vram was around 44 gigs, model changed to Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4). Even if I set the context window to smaller than 18000, less than half of what ollama capable to host using same size of Vram, the vllm backend would still report err: cuda out of memory. I was courious why Vllm would consume so much of Vram that even half the context ollama capable of serving would cause a Vram outage? ![image](https://github.com/user-attachments/assets/538beddf-2f9f-4669-bbc9-4603bbc77255) Vllm Err Msg ![image](https://github.com/user-attachments/ass...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Vram) for selfhosted API usage. And now I'm confused while switch from ollama to vllm. My sys is ubuntu 20.04 LTS. I was using ollama serving qwen2.5:32b-instruct_q4_K_M for couple of months. Set num_ctx to more than 32...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: around 44gb of vram. The problem comes when I tried to switch to vllm (docker, allocated the 2 2080ti gpus and available vram was around 44 gigs, model changed to Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4). Even if I set the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vram was around 44 gigs, model changed to Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4). Even if I set the context window to smaller than 18000, less than half of what ollama capable to host using same size of Vram, the vllm bac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wen/Qwen2.5-32B-Instruct-GPTQ-Int4). Even if I set the context window to smaller than 18000, less than half of what ollama capable to host using same size of Vram, the vllm backend would still report err: cuda out of me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi guys, I was using my home server(2x 2080Ti 22g + 1x Tesla P4 8g, total of 52gb Vram)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
