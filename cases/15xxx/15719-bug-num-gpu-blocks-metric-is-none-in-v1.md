# vllm-project/vllm#15719: [Bug]: num_gpu_blocks metric is None in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#15719](https://github.com/vllm-project/vllm/issues/15719) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: num_gpu_blocks metric is None in V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running vLLM openAI engine v0.8.1 on kubernetes (see the example yaml below). After vllm is running, I tried to get the metrics via ``` kubectl port-forward 8000 curl localhost:8000/metrics ``` And for vLLM V1, the `num_gpu_blocks` in `cache_config_info` is shown as `None`. After switching to vLLM V0, the metric shows the correct value. Is this a regression in V1? ``` # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_offload_gb="0",enable_prefix_caching="True",gpu_memory_utilization="0.9",is_attention_free="False",num_cpu_blocks="None",num_gpu_blocks="None",num_gpu_blocks_override="None",sliding_window="None",swap_space_bytes="4294967296"} 1.0 ``` ``` containers: - args: - --port - "8000" - --max-num-seqs - "2048" - --max_model_len - "4096" - --compilation-config - "3" - --tensor-parallel-size - "1" - --model - "meta-llama/Llama-2-7b-hf" - "--enable-lora" - "--max-loras" - "10" - "--max-cpu-loras" - "12" command: - python3 - -m - vllm.entrypoints.openai.api_server env: - name: PORT value: "8000" - name: HUGGING_FACE_HUB_TOKEN valueFrom: secretKeyRef:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: alhost:8000/metrics ``` And for vLLM V1, the `num_gpu_blocks` in `cache_config_info` is shown as `None`. After switching to vLLM V0, the metric shows the correct value. Is this a regression in V1? ``` # TYPE vllm:cache_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_offload_gb="0",enable_prefix_caching="True",gpu_memory_utilization="0.9",is_attention_free="False",nu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: num_gpu_blocks metric is None in V1 bug ### Your current environment ### 🐛 Describe the bug I am running vLLM openAI engine v0.8.1 on kubernetes (see the example yaml below). After vllm is running, I tried to get...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: fter switching to vLLM V0, the metric shows the correct value. Is this a regression in V1? ``` # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
