# vllm-project/vllm#38122: [Bug]: Qwen 3.5 fails to load from GGUF

| 字段 | 值 |
| --- | --- |
| Issue | [#38122](https://github.com/vllm-project/vllm/issues/38122) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen 3.5 fails to load from GGUF

### Issue 正文摘录

### Your current environment I can't get debug information from the container in my cluster as it constantly crashes and so I can't get a shell into it, but I'm just using the `docker.io/vllm/vllm-openai` image with following env: ``` Environment: PYTHONHASHSEED: 123 HF_HOME: /data POD_IP: (v1:status.podIP) PROMETHEUS_MULTIPROC_DIR: /tmp HF_TOKEN: Optional: false VLLM_NO_USAGE_STATS: 1 VLLM_ENGINE_ITERATION_TIMEOUT_S: 300 VLLM_DO_NOT_TRACK: 1 ``` I'm also quite sure I've already identified the issues, but don't quite know how to fix them myself. ### 🐛 Describe the bug When trying to load Qwen 3.5 from GGUF with the following command: ``` vllm serve unsloth/Qwen3.5-27B-GGUF:Q4_K_M --host 0.0.0.0 --port 8000 --no-enable-prefix-caching --max-model-len 48000 --gpu_memory_utilization 0.9 --tokenizer=Qwen/Qwen3.5-27B --hf-config-path=Qwen/Qwen3.5-27B --served-model-name=Qwen/Qwen3.5-27B --reasoning-parser=qwen3 --mm-encoder-tp-mode=data --mm-processor-cache-type=shm --enable-auto-tool-choice --tool-call-parser=qwen3_coder --trust-remote-code ``` It fails with "Unknown gguf model_type: qwen3_5", here it seems like it need the same replace workaround as `qwen3_moe` for example, as it's `q...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen 3.5 fails to load from GGUF bug ### Your current environment I can't get debug information from the container in my cluster as it constantly crashes and so I can't get a shell into it, but I'm just using the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ntly crashes and so I can't get a shell into it, but I'm just using the `docker.io/vllm/vllm-openai` image with following env: ``` Environment: PYTHONHASHSEED: 123 HF_HOME: /data POD_IP: (v1:status.podIP)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: DIR: /tmp HF_TOKEN: Optional: false VLLM_NO_USAGE_STATS: 1 VLLM_ENGINE_ITERATION_TIMEOUT_S: 300 VLLM_DO_NOT_TRACK: 1 ``` I'm also quite sure I've already identified the issues, but don't quite know how to
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f the model has or how to find out. I'm not that deep into the actual ML architecture. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: en3_5", here it seems like it need the same replace workaround as `qwen3_moe` for example, as it's `qwen35` in `gguf`: https://github.com/vllm-project/vllm/blob/6e37c46b35e2ee799fb280180f4d582219bea3f0/vllm/model_execut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
