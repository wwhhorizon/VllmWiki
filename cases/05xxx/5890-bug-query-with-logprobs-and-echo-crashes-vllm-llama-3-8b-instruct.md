# vllm-project/vllm#5890: [Bug]: Query with logprobs and echo crashes vllm (llama-3-8b-instruct)

| 字段 | 值 |
| --- | --- |
| Issue | [#5890](https://github.com/vllm-project/vllm/issues/5890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Query with logprobs and echo crashes vllm (llama-3-8b-instruct)

### Issue 正文摘录

### Your current environment ```text "image": "vllm/vllm-openai:latest" "options": "runtime=nvidia gpus=1 ipc=host" "--port=8000 --model=meta-llama/Meta-Llama-3-8B-Instruct --tensor-parallel-size=1 --disable-log-requests --enable-prefix-caching --gpu-memory-utilization=1", ``` vllm 5.0.0-post-1 ### 🐛 Describe the bug Running the following query: ``` '{"model": "meta-llama/Meta-Llama-3-8B-Instruct", "prompt": ["The following are multiple choice questions (with answers) about abstract algebra.\\nFind all c in Z_3 such that Z_3[x]/(x^2 + c) is a field.\\nA. 0\\nB. 1\\nC. 2\\nD. 3\\nAnswer: B\\n\\nStatement 1 | If aH is an element of a factor group, then |aH| divides |a|. Statement 2 | If H and K are subgroups of G then HK is a subgroup of G.\\nA. True, True\\nB. False, False\\nC. True, False\\nD. False, True\\nAnswer: B\\n\\nStatement 1 | Every element of a group generates a cyclic subgroup of the group. Statement 2 | The symmetric group S_10 has 10 elements.\\nA. True, True\\nB. False, False\\nC. True, False\\nD. False, True\\nAnswer: C\\n\\nStatement 1| Every function from a finite set onto itself must be one to one. Statement 2 | Every subgroup of an abelian group is abelian.\\nA....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: K are subgroups of G then HK is a subgroup of G.\\nA. True, True\\nB. False, False\\nC. True, False\\nD. False, True\\nAnswer: B\\n\\nStatement 1 | Every element of a group generates a cyclic subgroup of the group. Stat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Query with logprobs and echo crashes vllm (llama-3-8b-instruct) bug ### Your current environment ```text "image": "vllm/vllm-openai:latest" "options": "runtime=nvidia gpus=1 ipc=host" "--port=8000 --model=meta-ll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 6:20:13 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 06-26 06:20:13 async_llm_engine.py:52] File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 06-26 06:20:13 asy...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: a-llama/Meta-Llama-3-8B-Instruct --tensor-parallel-size=1 --disable-log-requests --enable-prefix-caching --gpu-memory-utilization=1", ``` vllm 5.0.0-post-1 ### 🐛 Describe the bug Running the following query: ``` '{"mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ) bug ### Your current environment ```text "image": "vllm/vllm-openai:latest" "options": "runtime=nvidia gpus=1 ipc=host" "--port=8000 --model=meta-llama/Meta-Llama-3-8B-Instruct --tensor-parallel-size=1 --disable-log-r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
