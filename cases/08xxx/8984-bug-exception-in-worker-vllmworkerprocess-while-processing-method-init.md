# vllm-project/vllm#8984: [Bug]: Exception in worker VllmWorkerProcess while processing method init_device: CUDA error: invalid device ordinal，vLLM并行多GPU搭载模型出错

| 字段 | 值 |
| --- | --- |
| Issue | [#8984](https://github.com/vllm-project/vllm/issues/8984) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Exception in worker VllmWorkerProcess while processing method init_device: CUDA error: invalid device ordinal，vLLM并行多GPU搭载模型出错

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 当我使用vllm进行多卡加速推理时，遇到了问题 我的参数设置如下： ``` 'generator': { 'model_name': 'llama2-7B-chat',#'llama3-8B-instruct',#'qwen2-7B-instruct', 'model_path': '/data00/yifei_chen/FlashRAG/models/shakechen/Llama-2-7b-chat-hf', 'type': torch.bfloat16, 'stop_token_ids': [151329, 151336, 151338], 'gpu_use':0.4, 'generator_params': { 'max_tokens': 512, 'temperature': 1, 'top_p': 0.7, } }, 'checker': { 'model_name': 'llama3-8B-instruct',#'glm-4-9b-chat',#', 'model_path': '/data00/LLaMA-3-8b-Instruct/', 'type': torch.bfloat16, 'stop_token_ids': [151329, 151336, 151338], 'gpu_use':0.55, 'generator_params': { # 'do_sample': True, # 'max_new_tokens': 2048, 'max_tokens': 512, 'temperature': 1, 'top_p': 0.7, 'top_k': 10, } }, ``` 我的服务器上的gpu如下： 模型初始化的代码如下： ``` models['generator'] = LLM( config['generator']['model_path'], dtype=config['generator']['type'], enforce_eager=True, trust_remote_code=True, max_model_len=4096, gpu_memory_utilization=config['generator']['gpu_use'], tensor_parallel_size=2, ) models['checker'] = LLM( config['checker']['model_path'], dtype=config['checker']['type'], enforce_eager=True, trust_remote_code...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ordinal，vLLM并行多GPU搭载模型出错 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 当我使用vllm进行多卡加速推理时，遇到了问题 我的参数设置如下： ``` 'generator': { 'model_name': 'llama2-7B-chat',#'llama3-8B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: put_proc=False) WARNING 10-01 10:44:26 multiproc_gpu_executor.py:56] Reducing Torch parallelism from 48 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: FlashRAG/models/shakechen/Llama-2-7b-chat-hf', 'type': torch.bfloat16, 'stop_token_ids': [151329, 151336, 151338], 'gpu_use':0.4, 'generator_params': { 'max_toke
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: hod init_device: CUDA error: invalid device ordinal，vLLM并行多GPU搭载模型出错 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 当我使用vllm进行多卡加速推理时，遇到了问题 我的参数设置如下： ``` 'generator': {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ception in worker VllmWorkerProcess while processing method init_device: CUDA error: invalid device ordinal，vLLM并行多GPU搭载模型出错 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
