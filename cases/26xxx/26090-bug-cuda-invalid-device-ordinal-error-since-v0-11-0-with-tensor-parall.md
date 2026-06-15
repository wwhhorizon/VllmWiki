# vllm-project/vllm#26090: [Bug]: Cuda invalid device ordinal error since v0.11.0 with tensor-parallel-size 2 with 2xH100

| 字段 | 值 |
| --- | --- |
| Issue | [#26090](https://github.com/vllm-project/vllm/issues/26090) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cuda invalid device ordinal error since v0.11.0 with tensor-parallel-size 2 with 2xH100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I'm currently running the **Qwen/Qwen3-30B-A3B-Instruct-2507-FP8** model on **2 × H100 GPUs** using **vLLM v0.10.2**. It works fine with the following command-line arguments: ``` --disable-log-stats --disable-log-requests --model Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 --max-model-len 131072 --gpu-memory-utilization 0.9 --swap-space 8 --dtype auto --kv-cache-dtype fp8 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes ``` However, when I switch the model to **Qwen/Qwen3-Next-80B-A3B-Instruct-FP8** and use the **vLLM nightly** build with the exact same arguments, I encounter an error. The model runs successfully only when I set ```--tensor-parallel-size 1```. Could you help me understand why this happens? Is there a known issue with tensor parallelism for the 80B model in the nightly version? ``` ERROR 10-02 04:36:58 [multiproc_executor.py:597] WorkerProc failed to start. ERROR 10-02 04:36:58 [multiproc_executor.py:597] Traceback (most recent call last): ERROR 10-02 04:36:58 [multiproc_executor.py:597] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 571, in wor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: to **Qwen/Qwen3-Next-80B-A3B-Instruct-FP8** and use the **vLLM nightly** build with the exact same arguments, I encounter an error. The model runs successfully only when I set ```--tensor-parallel-size 1```. Could you h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Cuda invalid device ordinal error since v0.11.0 with tensor-parallel-size 2 with 2xH100 bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I'm currently running the **Qwen/Qwen3-30B-A3B-Instruct-25...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e bug Hi, I'm currently running the **Qwen/Qwen3-30B-A3B-Instruct-2507-FP8** model on **2 × H100 GPUs** using **vLLM v0.10.2**. It works fine with the following command-line arguments: ``` --disable-log-stats --disable-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment ### 🐛 Describe the bug Hi, I'm currently running the **Qwen/Qwen3-30B-A3B-Instruct-2507-FP8** model on **2 × H100 GPUs** using **vLLM v0.10.2**. It works fine with the following command-line arguments: ``` -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ordinal error since v0.11.0 with tensor-parallel-size 2 with 2xH100 bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I'm currently running the **Qwen/Qwen3-30B-A3B-Instruct-2507-FP8** model on **2 × H10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
