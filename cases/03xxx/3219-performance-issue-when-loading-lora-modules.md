# vllm-project/vllm#3219: Performance issue when loading lora modules

| 字段 | 值 |
| --- | --- |
| Issue | [#3219](https://github.com/vllm-project/vllm/issues/3219) |
| 状态 | closed |
| 标签 | help wanted;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Performance issue when loading lora modules

### Issue 正文摘录

I compared two ways to launch the server. The model is vicuna-7b, and GPU is 2 \* A30. and the 1st way is ``` python -m vllm.entrypoints.openai.api_server \ --model /data/models/vicuna-7b-v1.5/ \ --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --enforce-eager --disable-log-requests ``` The 2nd way is: ``` python -m vllm.entrypoints.openai.api_server \ --model /data/models/vicuna-7b-v1.5/ \ --max-loras 16 --tensor-parallel-size 2 --max-lora-rank 64 --gpu-memory-utilization 0.9 \ --enable-lora --enforce-eager --disable-log-requests --lora-modules lora1=/root/path1/ lora2=/root/path2/ ... ``` In both tests, I send the same request, which sets the model as `/data/models/vicuna-7b-v1.5/`. But the performance differs a lot. ![image](https://uploads.linear.app/342cff15-f40f-4cf7-8bee-343d25adb534/0421c1bd-2196-4601-80e3-62d2f9769277/83c5b379-57ba-4acd-a1ce-a9004ddf41bf?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC8wNDIxYzFiZC0yMTk2LTQ2MDEtODBlMy02MmQyZjk3NjkyNzcvODNjNWIzNzktNTdiYS00YWNkLWExY2UtYTkwMDRkZGY0MWJmIiwiaWF0IjoxNzEwMzUyODIwLCJleHAiOjMzMjgwOTEyODIwfQ.EldgJUs7c_4w7DsWm5od4iLrtv_T9FeDlkJ1lH7EYXE)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Performance issue when loading lora modules help wanted;stale I compared two ways to launch the server. The model is vicuna-7b, and GPU is 2 \* A30. and the 1st way is ``` python -m vllm.entrypoints.openai.api_server \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1-80e3-62d2f9769277/83c5b379-57ba-4acd-a1ce-a9004ddf41bf?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC8wNDIxYzFiZC0yMTk2LTQ2MDEtODBlMy02MmQyZjk3NjkyNzcvODN...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: modules help wanted;stale I compared two ways to launch the server. The model is vicuna-7b, and GPU is 2 \* A30. and the 1st way is ``` python -m vllm.entrypoints.openai.api_server \ --model /data/models/vicuna-7b-v1.5/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s --lora-modules lora1=/root/path1/ lora2=/root/path2/ ... ``` In both tests, I send the same request, which sets the model as `/data/models/vicuna-7b-v1.5/`. But the performance differs a lot. ![image](https://uploads....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
