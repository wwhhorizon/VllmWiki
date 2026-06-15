# vllm-project/vllm#579: Key Error when handle multiple requests simultaneously

| 字段 | 值 |
| --- | --- |
| Issue | [#579](https://github.com/vllm-project/vllm/issues/579) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Key Error when handle multiple requests simultaneously

### Issue 正文摘录

After building a flask service while vllm as the LLM model, when i test the service with multiple requests simutaneously, it raise key error at scheduler.py Traceback (most recent call last): File "/web/anaconda3/envs/vllm/lib/python3.8/site-packages/flask/app.py", line 2190, in wsgi_app response = self.full_dispatch_request() File "/web/anaconda3/envs/vllm/lib/python3.8/site-packages/flask/app.py", line 1486, in full_dispatch_request rv = self.handle_user_exception(e) File "/web/anaconda3/envs/vllm/lib/python3.8/site-packages/flask/app.py", line 1484, in full_dispatch_request rv = self.dispatch_request() File "/web/anaconda3/envs/vllm/lib/python3.8/site-packages/flask/app.py", line 1469, in dispatch_request return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args) File "JZ_service_vllm.py", line 184, in get_response outputs = vllm_model.generate([system_prompt], sampling_params, use_tqdm=False) # , use_tqdm=False File "/root/vllm/vllm/entrypoints/llm.py", line 130, in generate return self._run_engine(use_tqdm) File "/root/vllm/vllm/entrypoints/llm.py", line 150, in _run_engine step_outputs = self.llm_engine.step() File "/root/vllm/vllm/engine/llm_engine.py", line 3...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Key Error when handle multiple requests simultaneously After building a flask service while vllm as the LLM model, when i test the service with multiple requests simutaneously, it raise key error at scheduler.py Traceba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -packages/flask/app.py", line 2190, in wsgi_app response = self.full_dispatch_request() File "/web/anaconda3/envs/vllm/lib/python3.8/site-packages/flask/app.py", line 1486, in full_dispatch_request rv = self.handle_user...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Key Error when handle multiple requests simultaneously After building a flask service while vllm as the LLM model, when i test the service with multiple requests simutaneously, it raise key error at scheduler.py Traceba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tputs = vllm_model.generate([system_prompt], sampling_params, use_tqdm=False) # , use_tqdm=False File "/root/vllm/vllm/entrypoints/llm.py", line 130, in generate return self._run_engine(use_tqdm) File "/root/vllm/vllm/e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ests simultaneously After building a flask service while vllm as the LLM model, when i test the service with multiple requests simutaneously, it raise key error at scheduler.py Traceback (most recent call last): File "/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
