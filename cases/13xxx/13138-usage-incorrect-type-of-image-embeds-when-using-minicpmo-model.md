# vllm-project/vllm#13138: [Usage]: Incorrect type of image_embeds when using minicpmo model

| 字段 | 值 |
| --- | --- |
| Issue | [#13138](https://github.com/vllm-project/vllm/issues/13138) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Incorrect type of image_embeds when using minicpmo model

### Issue 正文摘录

### Your current environment ```sh outputs = self.llm.generate( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/utils.py", line 1086, in inner return fn(*args, **kwargs) File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 461, in generate self._validate_and_add_requests( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1323, in _validate_and_add_requests self._add_request( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1341, in _add_request self.llm_engine.add_request( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/utils.py", line 1086, in inner return fn(*args, **kwargs) File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 751, in add_request preprocessed_inputs = self.input_preprocessor.preprocess( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packages/vllm/inputs/preprocess.py", line 676, in preprocess return self._process_decoder_o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Incorrect type of image_embeds when using minicpmo model usage;stale ### Your current environment ```sh outputs = self.llm.generate( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Incorrect type of image_embeds when using minicpmo model usage;stale ### Your current environment ```sh outputs = self.llm.generate( File "/data/DevEnvironments/miniconda/envs/minicpmo/lib/python3.10/site-packa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is a problem when integrating it with vllm and here is the code. ```py import os import uuid import uvicorn import traceback from transformers import AutoTokenizer from decord import VideoReader, cpu from PIL import Ima...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: stop_token_ids=self.stop_token_ids, # use_beam_search=False, temperature=0.4, top_p=0.8, top_k=100, max_tokens=2048, ) def infer_video(self, video_path, query, frames_num=MAX_NUM_FRAMES): frames = enc
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: stop_token_ids=self.stop_token_ids, # use_beam_search=False, temperature=0.4, top_p=0.8, top_k=100, max_tokens=2048, ) def infer_video(self, video_path, query, frames_num=MAX_NUM_FRAMES): frames = encode_vid

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
