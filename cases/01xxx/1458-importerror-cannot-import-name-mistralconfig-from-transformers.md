# vllm-project/vllm#1458: ImportError: cannot import name 'MistralConfig' from 'transformers'

| 字段 | 值 |
| --- | --- |
| Issue | [#1458](https://github.com/vllm-project/vllm/issues/1458) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: cannot import name 'MistralConfig' from 'transformers'

### Issue 正文摘录

I get this error trying to run a server with a llama-2 model. Also, is this the correct way to state I want the model quantized? Something else is that it refuses to work with the latest tokenizers. It only works with the exact version tokenizers==0.13.4rc3 peter@desktop:~$ python3 -m vllm.entrypoints.api_server -q awq --model lmsys/vicuna-13b-v1.3 Downloading (…)lve/main/config.json: 100%|██████████████████████████████████████████████████████████████████████████| 567/567 [00:00 . This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565 Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/api_server.py", line 74, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 487, in from_engine_args engine = cls(engine_args....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ImportError: cannot import name 'MistralConfig' from 'transformers' I get this error trying to run a server with a llama-2 model. Also, is this the correct way to state I want the model quantized? Something else is that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ImportError: cannot import name 'MistralConfig' from 'transformers' I get this error trying to run a server with a llama-2 model. Also, is this the correct way to state I want the model quantized? Something else is that
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: is this the correct way to state I want the model quantized? Something else is that it refuses to work with the latest tokenizers. It only works with the exact version tokenizers==0.13.4rc3 peter@desktop:~$ python3 -m v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: a llama-2 model. Also, is this the correct way to state I want the model quantized? Something else is that it refuses to work with the latest tokenizers. It only works with the exact version tokenizers==0.13.4rc3 peter@...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565 Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
