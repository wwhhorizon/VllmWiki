# vllm-project/vllm#9238: [Performance]: qwen2vl very slow when preprocess large image

| 字段 | 值 |
| --- | --- |
| Issue | [#9238](https://github.com/vllm-project/vllm/issues/9238) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: qwen2vl very slow when preprocess large image

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression build with latest vllm code and start Qwen2-VL-7B-Instruct ![image](https://github.com/user-attachments/assets/2f8e4aa4-0789-4e82-8920-b4180075f53d) It takes too long time to handle preprocess lead to heartbeat timeout. ERROR 10-10 01:14:54 client.py:250] RuntimeError('Engine loop has died') ERROR 10-10 01:14:54 client.py:250] Traceback (most recent call last): ERROR 10-10 01:14:54 client.py:250] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/client.py", line 150, in run_heartbeat_loop ERROR 10-10 01:14:54 client.py:250] await self._check_success( ERROR 10-10 01:14:54 client.py:250] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/client.py", line 314, in _check_success ERROR 10-10 01:14:54 client.py:250] raise response ERROR 10-10 01:14:54 client.py:250] RuntimeError: Engine loop has died ERROR 10-10 01:25:08 client.py:250] TimeoutError('No heartbeat received from MQLLMEngine') ERROR 10-10 01:25:08 client.py:250] NoneType: None DEBUG 10-10 01:25:08 client.py:144] Shutting down MQLLMEngineClient check health loop due to timeout DEBUG 10-10 01:2...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression build with latest vllm code and start Qwen2-VL-7B-Instruct ![image](https://github.com/user-attachments/assets/2f8e4aa4-0789-4e82-8920-b4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mprove performance _No response_ ### Report of performance regression build with latest vllm code and start Qwen2-VL-7B-Instruct ![image](https://github.com/user-attachments/assets/2f8e4aa4-0789-4e82-8920-b4180075f53d)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: qwen2vl very slow when preprocess large image performance ### Proposal to improve performance _No response_ ### Report of performance regression build with latest vllm code and start Qwen2-VL-7B-Instruct...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ent check health loop due to timeout DEBUG 10-10 01:25:14 client.py:170] Waiting for output from MQLLMEngine. CRITICAL 10-10 01:25:14 launcher.py:99] MQLLMEngine is already dead, terminating server process Any suggestio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
