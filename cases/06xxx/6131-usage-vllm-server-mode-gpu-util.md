# vllm-project/vllm#6131: [Usage]: vllm server mode, gpu util

| 字段 | 值 |
| --- | --- |
| Issue | [#6131](https://github.com/vllm-project/vllm/issues/6131) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm server mode, gpu util

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm using vllm `0.4.0.post1`, and I want to use [Llama3-8b-instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) to infer a lot of data. As the pieces of data have dependencies, I cannot use vllm directly, so I start the server mode. However, I note that my GPU-UTIL is constantly below 50% (8xA100-40G). I think it is due to small prompt queue passed to vllm server, so I use multiprocessing.Queue and concurrent.futures import ThreadPoolExecutor to infer parallelly and set **Count(Progress) * Count(Thread) = 1000**. And the GPU-UTIL is still below 50%. I want to fully utilize my gpu, but I don't know whether it is a feature of vllm. Thanks for your time!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -8B-Instruct) to infer a lot of data. As the pieces of data have dependencies, I cannot use vllm directly, so I start the server mode. However, I note that my GPU-UTIL is constantly below 50% (8xA100-40G). I think it is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: erver mode. However, I note that my GPU-UTIL is constantly below 50% (8xA100-40G). I think it is due to small prompt queue passed to vllm server, so I use multiprocessing.Queue and concurrent.futures import ThreadPoolEx...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d you like to use vllm I'm using vllm `0.4.0.post1`, and I want to use [Llama3-8b-instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) to infer a lot of data. As the pieces of data have dependencies, I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: is constantly below 50% (8xA100-40G). I think it is due to small prompt queue passed to vllm server, so I use multiprocessing.Queue and concurrent.futures import ThreadPoolExecutor to infer parallelly and set **Count(Pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
