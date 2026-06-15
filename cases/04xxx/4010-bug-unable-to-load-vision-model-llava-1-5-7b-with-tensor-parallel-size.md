# vllm-project/vllm#4010: [Bug]: Unable to load vision model llava 1.5 7b with tensor-parallel-size > 1 using vllm 0.4.0.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#4010](https://github.com/vllm-project/vllm/issues/4010) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to load vision model llava 1.5 7b with tensor-parallel-size > 1 using vllm 0.4.0.post1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug My expectation is that the model should properly load the language portion of the model into the different gpus i have available. error: `AssertionError: Provide `image_input_type` and other vision related configurations through LLM entrypoint or engine arguments.` But I seem to be providing it based on the example tests we have. ``` from vllm import LLM model = LLM( model="llava-hf/llava-1.5-7b-hf", image_input_type="pixel_values", download_dir="/tmp/models", image_token_id=32000, image_input_shape="1,3,336,336", image_feature_size=576, tensor_parallel_size=2 ) ``` (RayWorkerVllm pid=23847) ERROR 04-11 13:22:43 ray_utils.py:44] Error executing method load_model. This might cause deadlock in distributed execution. (RayWorkerVllm pid=23847) ERROR 04-11 13:22:43 ray_utils.py:44] Traceback (most recent call last): (RayWorkerVllm pid=23847) ERROR 04-11 13:22:43 ray_utils.py:44] File "/local_disk0/.ephemeral_nfs/envs/pythonEnv-8b85b5ac-0966-40f5-8881-cf111940a211/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 37, in execute_method (RayWorkerVllm pid=23847) ERROR 04-11 13:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unable to load vision model llava 1.5 7b with tensor-parallel-size > 1 using vllm 0.4.0.post1 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug My expectati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: em to be providing it based on the example tests we have. ``` from vllm import LLM model = LLM( model="llava-hf/llava-1.5-7b-hf", image_input_type="pixel_values", download_dir="/tmp/models", image_token_id=32000, image_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: :43 ray_utils.py:44] Error executing method load_model. This might cause deadlock in distributed execution. (RayWorkerVllm pid=23847) ERROR 04-11 13:22:43 ray_utils.py:44] Traceback (most recent call last): (RayWorkerVl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: engine arguments.` But I seem to be providing it based on the example tests we have. ``` from vllm import LLM model = LLM( model="llava-hf/llava-1.5-7b-hf", image_input_type="pixel_values", download_dir="/tmp/models", i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
