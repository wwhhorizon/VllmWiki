# vllm-project/vllm#2217: Error when Running HIPGraph with TP 8

| 字段 | 值 |
| --- | --- |
| Issue | [#2217](https://github.com/vllm-project/vllm/issues/2217) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error when Running HIPGraph with TP 8

### Issue 正文摘录

Command that was run: ``` python benchmark_throughput.py -tp 8 --model meta-llama_Llama-2-70b-chat-hf --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` Error Logs: ``` ... ensor_parallel_size=8, quantization=None, enforce_eager=False, seed=0) (RayWorkerVllm pid=343834) WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: (RayWorkerVllm pid=343834) PyTorch 2.1.1+cu121 with CUDA 1201 (you have 2.1.1+rocm5.6) (RayWorkerVllm pid=343834) Python 3.10.13 (you have 3.10.13) (RayWorkerVllm pid=343834) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) (RayWorkerVllm pid=343834) Memory-efficient attention, SwiGLU, sparse and more won't be available. (RayWorkerVllm pid=343834) Set XFORMERS_MORE_DETAILS=1 for more details INFO 12-20 08:54:51 llm_engine.py:223] # GPU blocks: 64920, # CPU blocks: 6553 (RayWorkerVllm pid=343834) INFO 12-20 08:54:51 model_runner.py:394] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. (RayWorkerVllm pid=343834) [W HIPGraph.cpp:146] W...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: (RayWorkerVllm pid=343834) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) (RayWorkerVllm pid=343834) Memory-efficient attent
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Error when Running HIPGraph with TP 8 rocm Command that was run: ``` python benchmark_throughput.py -tp 8 --model meta-llama_Llama-2-70b-chat-hf --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` Error Logs: ``` .....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 8 rocm Command that was run: ``` python benchmark_throughput.py -tp 8 --model meta-llama_Llama-2-70b-chat-hf --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` Error Logs: ``` ... ensor_parallel_size=8, quantizatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: (RayWorkerVllm pid=343834) [W HIPGraph.cpp:146] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator()) (RayWorkerVllm pid=343839) WARNING[XFORMERS]: xFormers can't load C++...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: or when Running HIPGraph with TP 8 rocm Command that was run: ``` python benchmark_throughput.py -tp 8 --model meta-llama_Llama-2-70b-chat-hf --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` Error Logs: ``` ... e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
