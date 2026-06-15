# vllm-project/vllm#9364: [Bug]: 400 Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#9364](https://github.com/vllm-project/vllm/issues/9364) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 400 Bad Request

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have following info in the log when I use Cling with vLLM: INFO: 10.147.113.100:54034 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request What should be changed in vLLM or in Cling to fix this? There is no other information in the logs. Command I use to run vLLM: docker run --runtime nvidia --gpus all --shm-size 64g -d --name vllm-Qwen25-72B-Instruct --restart unless-stopped -v ~/.cache/huggingface:/root/.cache/huggingface -e VLLM_USE_CPU_KV_CACHE=True -p 8000:8000 --ipc=host vllm/vllm-openai:v0.6.2 --model Qwen/Qwen2.5-72B-Instruct-AWQ --served-model-name BSSTelcoChat_Qwen2.5 --trust-remote-code --enable-prompt-adapter --max-prompt-adapters 8 --max-prompt-adapter-token 512 --enable-prefix-caching --max-num-seqs 8 --max-model-len 7168 --max-num-batched-tokens 7168 --max-seq-len-to-capture 7168 --block-size 32 --swap-space 32 --tensor-parallel-size 1 --pipeline-parallel-size 1 --gpu-memory-utilization 0.9999 --seed 44 --max-log-len 35 --use-v2-block-manager --enable-auto-tool-choice --tool-call-parser hermes --tokenizer-pool-size 16 --max-parallel-loading-workers 16 --num-lookahead-slots 12...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ? There is no other information in the logs. Command I use to run vLLM: docker run --runtime nvidia --gpus all --shm-size 64g -d --name vllm-Qwen25-72B-Instruct --restart unless-stopped -v ~/.cache/huggingface:/root/.ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: 400 Bad Request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have following info in the log when I use Cling with vLLM: INFO: 10.147.113.100:54034 - "POST /v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 400 Bad Request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have following info in the log when I use Cling with vLLM: INFO: 10.147.113.100:54034 - "POST /v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: l-len 7168 --max-num-batched-tokens 7168 --max-seq-len-to-capture 7168 --block-size 32 --swap-space 32 --tensor-parallel-size 1 --pipeline-parallel-size 1 --gpu-memory-utilization 0.9999 --seed 44 --max-log-len 35 --use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ahead-slots 12 --enable-chunked-prefill --disable-logprobs true --device cuda vLLM working properly with other tools the error is only with Cling https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
