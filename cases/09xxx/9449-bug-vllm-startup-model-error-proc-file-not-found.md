# vllm-project/vllm#9449: [Bug]: vllm startup model error /proc file not found

| 字段 | 值 |
| --- | --- |
| Issue | [#9449](https://github.com/vllm-project/vllm/issues/9449) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm startup model error /proc file not found

### Issue 正文摘录

### Your current environment python 3.10 vllm=0.4.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Because the prompt sent to the model was too long, it caused the model error, I shut down and restarted, and kept reporting this error, restarting the server, and cleaning the ray cache seemed to be of no use. How to solve, vllm error log how to read? The specific errors are as follows: ``` (policy_clone) zhengzhenzhuang@n35192:~/liujian/project$ python -m vllm.entrypoints.openai.api_server --model /home/zhengzhenzhuang/liujian/model/Qwen2.5-72B-Instruct-GPTQ-Int8 --host 192.168.80.35 --tensor-parallel-size 8 --trust-remote-code INFO 10-17 07:23:53 gptq_marlin.py:133] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. Traceback (most recent call last): File "/home/zhengzhenzhuang/.conda/envs/policy_clone/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/home/zhengzhenzhuang/.conda/envs/policy_clone/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/zhengzhenzhuang/.conda/envs/policy_clone/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm startup model error /proc file not found bug;stale ### Your current environment python 3.10 vllm=0.4.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Because the prompt sent to the model was too...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ite-packages/psutil/_common.py", line 841, in bcat return cat(fname, fallback=fallback, _open=open_binary) File "/home/zhengzhenzhuang/.conda/envs/policy_clone/lib/python3.10/site-packages/psutil/_common.py", line 829,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eemed to be of no use. How to solve, vllm error log how to read? The specific errors are as follows: ``` (policy_clone) zhengzhenzhuang@n35192:~/liujian/project$ python -m vllm.entrypoints.openai.api_server --model /hom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm startup model error /proc file not found bug;stale ### Your current environment python 3.10 vllm=0.4.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Because the prompt sent to the model was too...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
