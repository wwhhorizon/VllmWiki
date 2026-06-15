# vllm-project/vllm#8693: [Bug]: Pixtral-12B not supported on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#8693](https://github.com/vllm-project/vllm/issues/8693) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pixtral-12B not supported on CPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running into an error when trying to run Pixtral12B on CPU. Here is the sample code I am using: ```python from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "mistralai/Pixtral-12B-2409" sampling_params = SamplingParams(max_tokens=8192) llm = LLM(model=model_name, tokenizer_mode="mistral") prompt = "Describe this image in one sentence." image_url = "https://picsum.photos/id/237/200/300" messages = [ { "role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": image_url}}] }, ] outputs = llm.chat(messages, sampling_params=sampling_params) print(outputs[0].outputs[0].text) ``` And here is the output of the program: ``` python3 main.py WARNING 09-21 15:31:18 _custom_ops.py:18] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') INFO 09-21 15:31:19 config.py:1653] Downcasting torch.float32 to torch.float16. WARNING 09-21 15:31:19 arg_utils.py:910] The model has a long context length (128000). This may cause OOM errors during the initial memory profil...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ixtral-12B not supported on CPU bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running into an error when trying to run Pixtral12B on CPU. Here is the sample code I am u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: xtral12B on CPU. Here is the sample code I am using: ```python from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "mistralai/Pixtral-12B-2409" sampling_params = SamplingParams(max_tokens=8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ile or directory') INFO 09-21 15:31:19 config.py:1653] Downcasting torch.float32 to torch.float16. WARNING 09-21 15:31:19 arg_utils.py:910] The model has a long context length (128000). This may cause OOM errors during...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 18 _custom_ops.py:18] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') INFO 09-21 15:31:19 config.py:1653] Downcasting torch.float32 to torch.floa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
