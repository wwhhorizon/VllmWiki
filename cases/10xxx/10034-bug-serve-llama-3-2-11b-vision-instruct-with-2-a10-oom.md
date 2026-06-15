# vllm-project/vllm#10034: [Bug]: serve Llama-3.2-11B-Vision-Instruct with 2 A10 oom

| 字段 | 值 |
| --- | --- |
| Issue | [#10034](https://github.com/vllm-project/vllm/issues/10034) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: serve Llama-3.2-11B-Vision-Instruct with 2 A10 oom

### Issue 正文摘录

### Your current environment docker image vllm/vllm-openai:v0.6.2 and vllm/vllm-openai:v0.6.3 command：docker run --runtime nvidia --gpus '"device=0,1"' -d -v /data/model/llama:/data/model/llama -p 8001:8000 vllm/vllm-openai:v0.6.2 --model /data/model/llama --max-model-len 1024 --served_model_name Llama-3.2-11B-Vision-Instruct --tensor-parallel-size 2 --gpu_memory_utilization 0.7 I tried v0.6.2 and v0.6.3，both not work，only half of the gpu memory is occupied nvidia-smi output： +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 555.42.06 Driver Version: 555.42.06 CUDA Version: 12.5 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A10 On | 00000000:00:04.0 Off | 0 | | 0% 47C P0 60W / 150W | 10797MiB / 23028MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=False, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 3.2-11B-Vision-Instruct with 2 A10 oom bug ### Your current environment docker image vllm/vllm-openai:v0.6.2 and vllm/vllm-openai:v0.6.3 command：docker run --runtime nvidia --gpus '"device=0,1"' -d -v /data/model/llama:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=1024, guided_decoding_backend='outlines', distributed_executor_ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: serve Llama-3.2-11B-Vision-Instruct with 2 A10 oom bug ### Your current environment docker image vllm/vllm-openai:v0.6.2 and vllm/vllm-openai:v0.6.3 command：docker run --runtime nvidia --gpus '"device=0,1"' -d -v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and v0.6.3，both not work，only half of the gpu memory is occupied nvidia-smi output： +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 555.42.06 Driver Version: 555....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
