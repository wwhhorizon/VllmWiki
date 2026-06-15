# vllm-project/vllm#25176: [Bug]: Internvl3-2B/8B can't inference with video input when combined with AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#25176](https://github.com/vllm-project/vllm/issues/25176) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Internvl3-2B/8B can't inference with video input when combined with AsyncLLMEngine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am trying to use the internvl3-2B/8B (both have qwen 2.5 text backbone and support video input) to take in video input. That works out of the box on offline inference (I am testing out on this https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py#L594-L630). However, when I tried to deploy the model with AsyncLLMEngine, it complains about supported number of video input is 0. Here is my code for the AsyncLLMEngine ``` import numpy as np from transformers import AutoModel, AutoTokenizer from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput from vllm import __version__ as vllm_version from vllm.entrypoints.chat_utils import ( ChatCompletionContentPartParam, apply_hf_chat_template, parse_chat_messages, resolve_chat_template_content_format, ) from vllm.inputs import TextPrompt from vllm.sampling_params import GuidedDecodingParams, RequestOutputKind, SamplingParams from vllm.utils import FlexibleArgumentParser tokenizer = AutoTokenizer.from_pretrained( "OpenGVLab/InternVL3-8B", trust_remote_code=True, use_fast=False, ) args = ["--model", "OpenGVLab/InternVL3-8B", *self.worker_conf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Internvl3-2B/8B can't inference with video input when combined with AsyncLLMEngine bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I am trying to use the internvl3-2B/8B (both have qwen 2.5 text...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: number of video input is 0. Here is my code for the AsyncLLMEngine ``` import numpy as np from transformers import AutoModel, AutoTokenizer from vllm import AsyncEngineArgs, AsyncLLMEngine, RequestOutput from vllm impor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: B can't inference with video input when combined with AsyncLLMEngine bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I am trying to use the internvl3-2B/8B (both have qwen 2.5 text backbone and support...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: *self.worker_config.args, "--max-model-len", "16k", "--guided-decoding-backend", "xgrammar", "--enable-prefix-caching"] args_parser = AsyncEngineArgs.add_cli_args(FlexibleArgumentParser()) parsed_args = args_parser.pars...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ti_modal_data": { "video": np.zeros((10,448,448, 3), dtype=np.uint8) # any video data put here is ok }, } sampling_params = SamplingParams( temperature=self.temperature, max_tokens=1, logprobs=10, ) request_id = "0000"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
