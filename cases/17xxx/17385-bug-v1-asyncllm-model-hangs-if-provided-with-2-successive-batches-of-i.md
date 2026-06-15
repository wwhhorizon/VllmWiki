# vllm-project/vllm#17385: [Bug]: v1 AsyncLLM model hangs if provided with 2 successive batches of items to process

| 字段 | 值 |
| --- | --- |
| Issue | [#17385](https://github.com/vllm-project/vllm/issues/17385) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 AsyncLLM model hangs if provided with 2 successive batches of items to process

### Issue 正文摘录

### Your current environment Possibly relevant packages from pip list ``` Package Version Editable project location ---------------------------------------- ------------- ------------------------- accelerate 1.6.0 huggingface-hub 0.30.2 mistral_common 1.5.4 nest_asyncio 1.6.0 numpy 1.26.4 nvidia-cublas-cu12 12.4.5.8 nvidia-cuda-cupti-cu12 12.4.127 nvidia-cuda-nvrtc-cu12 12.4.127 nvidia-cuda-runtime-cu12 12.4.127 nvidia-cudnn-cu12 9.1.0.70 nvidia-cufft-cu12 11.2.1.3 nvidia-cufile-cu12 1.11.1.6 nvidia-curand-cu12 10.3.5.147 nvidia-cusolver-cu12 11.6.1.9 nvidia-cusparse-cu12 12.3.1.170 nvidia-cusparselt-cu12 0.6.2 nvidia-nccl-cu12 2.21.5 nvidia-nvjitlink-cu12 12.4.127 nvidia-nvtx-cu12 12.4.127 openai 1.55.2 pillow 11.2.1 pip 25.0.1 protobuf 3.20.3 pyarrow 19.0.1 pycountry 24.6.1 pycparser 2.22 pydantic 2.11.3 pydantic_core 2.33.1 ray 2.43.0 regex 2024.11.6 ruff 0.2.2 safetensors 0.5.3 stanza 1.10.1 starlette 0.46.2 tokenizers 0.21.1 torch 2.6.0 torchaudio 2.6.0 torchvision 0.21.0 tqdm 4.67.1 transformers 4.51.3 triton 3.2.0 urllib3 2.4.0 uvicorn 0.34.2 vllm 0.8.4 ``` Possibly relevant env vars ``` "VLLM_LOGGING_LEVEL":"DEBUG", "VLLM_TRACE_FUNCTION": "1", "CUBLAS_WORKSPACE_CONFIG": ":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ant packages from pip list ``` Package Version Editable project location ---------------------------------------- ------------- ------------------------- accelerate 1.6.0 huggingface-hub 0.30.2 mist
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v1 AsyncLLM model hangs if provided with 2 successive batches of items to process bug ### Your current environment Possibly relevant packages from pip list ``` Package Version Editable projec
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "model_name=,is_async=True,data_parallel_size=2,tensor_parallel_size=1,dtype=bfloat16,max_model_length=32768,max_num_batched_tokens=32768,gpu_memory_utilization=0.8,generation_parameters={max_new_tokens:32768,temperatur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 1.26.4 nvidia-cublas-cu12 12.4.5.8 nvidia-cuda-cupti-cu12 12.4.127 nvidia-cuda-nvrtc-cu12 12.4.127 nvidia-cuda-runtime-cu12 12.4.127 nvidia-cudnn-cu12 9.1.0.70 nvidia-cufft-cu12
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lm.v1.engine.async_llm import AsyncLLM from vllm import AsyncEngineArgs, RequestOutput, SamplingParams async def _async_one_item( model, params, index: str, ): output = await anext( model.generate(request_id=index, prom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
