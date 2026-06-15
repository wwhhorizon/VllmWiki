# vllm-project/vllm#17154: [Bug]: GLM-4-32B-0414-FP8 output !!!!! error (tensor is nan)

| 字段 | 值 |
| --- | --- |
| Issue | [#17154](https://github.com/vllm-project/vllm/issues/17154) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4-32B-0414-FP8 output !!!!! error (tensor is nan)

### Issue 正文摘录

### Your current environment image: vllm/vllm-openai:v0.8.4 Update glm4.py use this [pr](https://github.com/vllm-project/vllm/pull/16618/files#diff-12cee570cad925634eabcb0c4c44100f59f1a99a5038535d8742d51328681340). ```bash docker rm -f test-cuda sudo docker run -itd \ --gpus 2 \ --name=test-cuda \ -v /mnt/disk1/:/llm/models \ --net=host \ --privileged \ --shm-size="16g" \ --entrypoint /bin/bash \ vllm/vllm-openai:v0.8.4 ``` ### 🐛 Describe the bug I use two RTX 4090 cards to run GLM4 models. Running GLM-4-9B-0414, the output is normal. But running GLM-4-32B-0414-FP8, the output will be `!!!!!!` caused by nan error. ```python # example to reproduce # vllm_offline_inference.py from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="/llm/models/GLM-4-32B-0414-FP8", #model="/llm/models/GLM-4-9B-0414", device="cuda", dtype="float16", enforce_eager=True, tensor_parallel_size=2, gpu_memory_utilization=0.95, disable_async_output_proc=True, distributed_executor_backend="ray", max_model_len=3000, trust_remo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: cee570cad925634eabcb0c4c44100f59f1a99a5038535d8742d51328681340). ```bash docker rm -f test-cuda sudo docker run -itd \ --gpus 2 \ --name=test-cuda \ -v /mnt/disk1/:/llm/models \ --net=host \ --privileged \ --shm-size="1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: GLM-4-32B-0414-FP8 output !!!!! error (tensor is nan) bug ### Your current environment image: vllm/vllm-openai:v0.8.4 Update glm4.py use this [pr](https://github.com/vllm-project/vllm/pull/16618/files#diff-12cee5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cb0c4c44100f59f1a99a5038535d8742d51328681340). ```bash docker rm -f test-cuda sudo docker run -itd \ --gpus 2 \ --name=test-cuda \ -v /mnt/disk1/:/llm/models \ --net=host \ --privileged \ --shm-size="16g" \ --entrypoint...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: LLM engine (v0.8.4) with config: model='/llm/models/GLM-4-32B-0414-FP8', speculative_config=None, tokenizer='/llm/models/GLM-4-32B-0414-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: disable_async_output_proc=True, distributed_executor_backend="ray", max_model_len=3000, trust_remote_code=True, block_size=8, max_num_batched_tokens=3000) outputs = llm.generate(prompts, sampling_params) # Print the out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
