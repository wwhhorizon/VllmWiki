# vllm-project/vllm#14143: [Bug]: Failure to Init Qwen2VL-2B-Instruct with tensor-parallel-size == 4 and quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#14143](https://github.com/vllm-project/vllm/issues/14143) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failure to Init Qwen2VL-2B-Instruct with tensor-parallel-size == 4 and quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I am running the following command with Qwen2VL-2B model with `tensor-parallel-size=1`, then its working fine. But when I am running it with `tensor-parallel-size=4` (anything greater than 1), then I am getting `assert param_data.shape == loaded_weight.shape` this error? ``` VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server \ --served-model-name qwen-model \ --model /home/ec2-user/workspace/qwen_model_v1 \ --tensor-parallel-size 1 \ --max-model-len 32768 \ --gpu-memory-utilization 0.8 \ --max-num-seqs 20 \ --max-lora-rank 128 \ --enable-lora \ --lora-modules qwen-lora=/home/ec2-user/workspace/vllm/ckpt/qwen_one \ --lora-dtype float16 \ --task embed \ --dtype float16 \ --quantization bitsandbytes \ --load-format bitsandbytes \ --tensor-parallel-size 4 \ --seed 42 \ --port 8080 \ --override-pooler-config '{"pooling_type": "LAST", "normalize": false}' ``` What is the reason for the above. I have attached the following logs as well. ``` (VllmWorkerProcess pid=1947427) ERROR 03-03 15:10:13 multiproc_worker_utils.py:242] Exception in worker VllmWorkerProcess while processing method load_model. (VllmWorkerProces...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Failure to Init Qwen2VL-2B-Instruct with tensor-parallel-size == 4 and quantization bug;stale ### Your current environment ### 🐛 Describe the bug When I am running the following command with Qwen2VL-2B model with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : Failure to Init Qwen2VL-2B-Instruct with tensor-parallel-size == 4 and quantization bug;stale ### Your current environment ### 🐛 Describe the bug When I am running the following command with Qwen2VL-2B model with `ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: \ --override-pooler-config '{"pooling_type": "LAST", "normalize": false}' ``` What is the reason for the above. I have attached the following logs as well. ``` (VllmWorkerProcess pid=1947427) ERROR 03-03 15:10:13 multip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Qwen2VL-2B-Instruct with tensor-parallel-size == 4 and quantization bug;stale ### Your current environment ### 🐛 Describe the bug When I am running the following command with Qwen2VL-2B model with `tensor-parallel-size=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
