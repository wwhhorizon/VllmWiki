# vllm-project/vllm#1682: load_weights KeyError with quantized GPTBigCodeForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1682](https://github.com/vllm-project/vllm/issues/1682) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> load_weights KeyError with quantized GPTBigCodeForCausalLM

### Issue 正文摘录

I trying load awq quantized [bigcode/octocoder](https://huggingface.co/bigcode/octocoder) (GPTBigCodeForCausalLM) model wth vLLM. **Environ** - docker image based nvcr.io/nvidia/pytorch:23.08-py3 - CUDA 12.2.1 - pytorch 2.1.0a0+29c30b1 - transformers==4.35.0 - autoawq==0.1.6 - vllm local build from github sourece **repro** - quantize bigcode/octocoder with AutoAWQ - load model with Transformer and inferencing It works fine. - clone `refactor-quantization` branch from [PR1622](https://github.com/vllm-project/vllm/pull/1622) - try load model ``` Initializing an LLM engine with config: model='/usr/local/model/llm', tokenizer='/usr/local/model/llm', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, seed=0) ``` - RayWorker dead with Error ``` ray.exceptions.RayTaskError(KeyError): ray::RayWorker.execute_method() (pid=9510, ip=192.168.16.3, actor_id=9528afa7f50796c535e2572901000000, repr= ) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, **kwargs) File "/usr/loc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: igcode/octocoder) (GPTBigCodeForCausalLM) model wth vLLM. **Environ** - docker image based nvcr.io/nvidia/pytorch:23.08-py3 - CUDA 12.2.1 - pytorch 2.1.0a0+29c30b1 - transformers==4.35.0 - autoawq==0.1.6 - vllm local bu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: load_weights KeyError with quantized GPTBigCodeForCausalLM bug I trying load awq quantized [bigcode/octocoder](https://huggingface.co/bigcode/octocoder) (GPTBigCodeForCausalLM) model wth vLLM. **Environ** - docker image...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: eForCausalLM bug I trying load awq quantized [bigcode/octocoder](https://huggingface.co/bigcode/octocoder) (GPTBigCodeForCausalLM) model wth vLLM. **Environ** - docker image based nvcr.io/nvidia/pytorch:23.08-py3 - CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LM. **Environ** - docker image based nvcr.io/nvidia/pytorch:23.08-py3 - CUDA 12.2.1 - pytorch 2.1.0a0+29c30b1 - transformers==4.35.0 - autoawq==0.1.6 - vllm local build from github sourece **repro** - quantize bigcode/o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, seed=0) ``` - RayWorker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
