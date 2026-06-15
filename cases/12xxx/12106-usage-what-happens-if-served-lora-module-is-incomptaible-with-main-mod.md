# vllm-project/vllm#12106: [Usage]: what happens if served lora module is incomptaible with main model?

| 字段 | 值 |
| --- | --- |
| Issue | [#12106](https://github.com/vllm-project/vllm/issues/12106) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: what happens if served lora module is incomptaible with main model?

### Issue 正文摘录

### Your current environment N.A. ### How would you like to use vllm For example, I serve like this > VLLM_CACHE_ROOT=/home/cyg1sgh/temp CUDA_VISIBLE_DEVICES=1,2,3,4 VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve Qwen/Qwen2-VL-72B-Instruct --host 0.0.0.0 --port 8000 --tensor-parallel-size 4 --disable_custom_all_reduce --limit-mm-per-prompt "image=10" --quantization 'bitsandbytes' --load_format "bitsandbytes" --enable_lora --max_lora_rank 256 --lora-modules qlora=/home/cyg1sgh/qwen2-vl-72b-learn-0113/qlora_adapter_epoch0 qlora2="/home/cyg1sgh/qwen2-vl-7b-learn-0113/qlora_adapter_epoch0" qlora2 is incompatible with Qwen/Qwen2-VL-72B-Instruct but it still gives valid response without error. what happens under the hood in this situation? another question: is my serve method the correct way to serve qlora? i see that there is a `--qlora-adapter-name-or-path` param but it does not seem to be of any use. can someone advise on what is the correct way to serve qlora adapter train using 4-bit bitsandbytes qlora? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](htt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: what happens if served lora module is incomptaible with main model? usage;stale ### Your current environment N.A. ### How would you like to use vllm For example, I serve like this > VLLM_CACHE_ROOT=/home/cyg1sg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lm For example, I serve like this > VLLM_CACHE_ROOT=/home/cyg1sgh/temp CUDA_VISIBLE_DEVICES=1,2,3,4 VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve Qwen/Qwen2-VL-72B-Instruct --host 0.0.0.0 --port 8000 --tensor-parallel-s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: el-size 4 --disable_custom_all_reduce --limit-mm-per-prompt "image=10" --quantization 'bitsandbytes' --load_format "bitsandbytes" --enable_lora --max_lora_rank 256 --lora-modules qlora=/home/cyg1sgh/qwen2-vl-72b-learn-0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hat happens if served lora module is incomptaible with main model? usage;stale ### Your current environment N.A. ### How would you like to use vllm For example, I serve like this > VLLM_CACHE_ROOT=/home/cyg1sgh/temp CUD...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
