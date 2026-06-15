# vllm-project/vllm#15033: [Usage]: Can't pickle <class 'transformers_modules.configuration_phi4mm.Phi4MMConfig'>: it's not the same object as transformers_modules.configuration_phi4mm.Phi4MMConfig

| 字段 | 值 |
| --- | --- |
| Issue | [#15033](https://github.com/vllm-project/vllm/issues/15033) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can't pickle <class 'transformers_modules.configuration_phi4mm.Phi4MMConfig'>: it's not the same object as transformers_modules.configuration_phi4mm.Phi4MMConfig

### Issue 正文摘录

### Your current environment Code `vllm serve Phi-4-multimodal-instruct/ --port 12345 --host 0.0.0.0 --dtype bfloat16 --limit-mm-per-prompt image=10 --trust-remote-code --tensor-parallel-size 4 --max-model-len 20000` Error ``` File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 431, in run_mp_engine engine = MQLLMEngine.from_vllm_config( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 126, in from_vllm_config return cls( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 80, in __init__ self.engine = LLMEngine(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 280, in __init__ self.model_executor = executor_class(vllm_config=vllm_config, ) File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 271, in __init__ super().__init__(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 52, in __init__ self._init_executor() File "/usr/local/lib/python3.10/dist-packages/vllm/executor/mp_distributed_executor.py", line 90, in _init_executor worker = Pr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trypoints/openai/api_server.py", line 1007, in run_server async with build_async_engine_client(args) as engine_client: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de `vllm serve Phi-4-multimodal-instruct/ --port 12345 --host 0.0.0.0 --dtype bfloat16 --limit-mm-per-prompt image=10 --trust-remote-code --tensor-parallel-size 4 --max-model-len 20000` Error ``` File "/usr/local/lib/py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Can't pickle <class 'transformers_modules.configuration_phi4mm.Phi4MMConfig'>: it's not the same object as transformers_modules.configuration_phi4mm.Phi4MMConfig usage ### Your current environment Code `vllm se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0/dist-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_server(args)) Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
