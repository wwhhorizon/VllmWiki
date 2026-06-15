# vllm-project/vllm#363: RuntimeError: probability tensor contains either `inf`, `nan` or element < 0 when running mpt-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#363](https://github.com/vllm-project/vllm/issues/363) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: probability tensor contains either `inf`, `nan` or element < 0 when running mpt-7b

### Issue 正文摘录

Hi Everyone. I'm trying to use the fresh new MPT-7b included in vllm. I'm running on SageMaker Studio, in a g4dn.2xlarge instance, however, I'm getting the following error: `RuntimeError: probability tensor contains either `inf`, `nan` or element < 0` My code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="mosaicml/mpt-7b", dtype='float16') outputs = llm.generate(prompts, sampling_params) ### error happens here # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` This is my environment: ```bash accelerate @ file:///home/conda/feedstock_root/build_artifacts/accelerate_1683553934867/work aiofiles==23.1.0 aiohttp==3.8.4 aiosignal==1.3.1 altair==5.0.1 anyio==3.7.0 apex @ file:///apex appdirs==1.4.4 asttokens @ file:///home/conda/feedstock_root/build_artifacts/asttokens_1670263926556/work async-timeout==4.0.2 attrs==22.2.0 awscli @ file:///home/conda/feedstock_roo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ontains either `inf`, `nan` or element < 0` My code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: artifacts/numpy_1668919096861/work nvidia-cublas-cu11==11.10.3.66 nvidia-cuda-cupti-cu11==11.7.101 nvidia-cuda-nvrtc-cu11==11.7.99 nvidia-cuda-runtime-cu11==11.7.99 nvidia-cudnn-cu11==8.5.0.96 nvidia-cufft-cu11==10.9.0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="mosaicml/mpt-7b", dtype='float16') outputs = llm.generate(prompts, sampling_params) ### error happens here # Print the outputs. for output i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: gParams(temperature=0.8, top_p=0.95) llm = LLM(model="mosaicml/mpt-7b", dtype='float16') outputs = llm.generate(prompts, sampling_params) ### error happens here # Print the outputs. for output in outputs: prompt = outpu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: k_root/build_artifacts/traitlets_1675110562325/work transformers==4.28.1 triton==2.0.0 typer @ file:///home/conda/feedstock_root/build_artifacts/typer_1667832226065/work typing-inspect==0.9.0 typing_extensions @ file://...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
