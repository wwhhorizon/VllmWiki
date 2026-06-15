# vllm-project/vllm#3139: ModuleNotFoundError: No module named 'outlines.fsm'

| 字段 | 值 |
| --- | --- |
| Issue | [#3139](https://github.com/vllm-project/vllm/issues/3139) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ModuleNotFoundError: No module named 'outlines.fsm'

### Issue 正文摘录

python -m vllm.entrypoints.openai.api_server --model /datas/models/deepmoney-miqu-2-70b-awq --tensor-parallel-size 4 --enforce-eager --chat-template ./examples/template_chatml.jinja Traceback (most recent call last): File "/root/anaconda3/envs/vllm/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/root/anaconda3/envs/vllm/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/DATA4T/text-generation-webui/vllm/vllm/entrypoints/openai/api_server.py", line 22, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/DATA4T/text-generation-webui/vllm/vllm/entrypoints/openai/serving_chat.py", line 15, in from vllm.model_executor.guided_decoding import get_guided_decoding_logits_processor File "/DATA4T/text-generation-webui/vllm/vllm/model_executor/guided_decoding.py", line 12, in from vllm.model_executor.guided_logits_processors import JSONLogitsProcessor, RegexLogitsProcessor File "/DATA4T/text-generation-webui/vllm/vllm/model_executor/guided_logits_processors.py", line 23, in from outlines.fsm.fsm import RegexFSM ModuleNotFoundError: No module named 'outlines.fsm' CUDA12.1 installed...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _server.py", line 22, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/DATA4T/text-generation-webui/vllm/vllm/entrypoints/openai/serving_chat.py", line 15, in from vllm.model_executor.guided_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ModuleNotFoundError: No module named 'outlines.fsm' python -m vllm.entrypoints.openai.api_server --model /datas/models/deepmoney-miqu-2-70b-awq --tensor-parallel-size 4 --enforce-eager --chat-template ./examples/templat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dule named 'outlines.fsm' python -m vllm.entrypoints.openai.api_server --model /datas/models/deepmoney-miqu-2-70b-awq --tensor-parallel-size 4 --enforce-eager --chat-template ./examples/template_chatml.jinja Traceback (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
