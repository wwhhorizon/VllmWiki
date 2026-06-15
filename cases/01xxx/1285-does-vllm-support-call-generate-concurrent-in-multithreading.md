# vllm-project/vllm#1285: does vllm support call generate concurrent in multithreading?

| 字段 | 值 |
| --- | --- |
| Issue | [#1285](https://github.com/vllm-project/vllm/issues/1285) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> does vllm support call generate concurrent in multithreading?

### Issue 正文摘录

I use grpc server multithreading to do infer，but get error as fllowing File "/usr/local/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 130, in generate return self._run_engine(use_tqdm) File "/usr/local/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 150, in _run_engine step_outputs = self.llm_engine.step() File "/usr/local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 559, in step return self._process_model_outputs(output, scheduler_outputs) File "/usr/local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 518, in _process_model_outputs self._process_sequence_group_samples(seq_group, samples) File "/usr/local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 357, in _process_sequence_group_samples parent_child_dict[sample.parent_seq_id].append(sample) KeyError: 513 port = '8500' server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) predict_pb2_grpc.add_PredictServiceServicer_to_server(Predict(), server) server.add_insecure_port('[::]:' + port) server.start() logging.info("Starting server on %s", port) server.wait_for_termination()

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s/vllm/engine/llm_engine.py", line 559, in step return self._process_model_outputs(output, scheduler_outputs) File "/usr/local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 518, in _process_model_outputs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ne.py", line 559, in step return self._process_model_outputs(output, scheduler_outputs) File "/usr/local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 518, in _process_model_outputs self._process_sequence...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
