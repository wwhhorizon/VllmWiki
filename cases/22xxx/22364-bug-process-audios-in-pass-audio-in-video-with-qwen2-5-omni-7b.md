# vllm-project/vllm#22364: [Bug]: process audios in pass audio in video with qwen2.5-omni-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#22364](https://github.com/vllm-project/vllm/issues/22364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: process audios in pass audio in video with qwen2.5-omni-7b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug another bug when i test single video with audio. After process the audio, the dimension of "input_features" and "feature_attention_mask" doesn't match. The video exceeds ten minutes, maybe it is related. ```python def get_use_audio_in_video_query() -> QueryResult: question = ( "Describe the content of the video, then convert what the baby say into text." ) prompt = ( f" system\n{default_system} \n" " user\n " f"{question} \n" f" assistant\n" ) # from test import load_dataset # import os # saved_dataset_path = "dataset.pkl" # if os.path.exists(saved_dataset_path): # print(f"Found saved dataset at {saved_dataset_path}, loading...") # dataset_with_audio, dataset_without_audio = load_dataset(saved_dataset_path, format='pickle') # print(f"Loaded dataset with audio with {len(dataset_with_audio)} items.") # print(f"Loaded dataset without audio with {len(dataset_without_audio)} items.") # video = dataset_with_audio[4]['video'] # audio = dataset_with_audio[4]['audio'] from test import video_to_ndarrays import librosa video_path ="/home/jxchen/dataset/SafeWatch/real/videos/C1/hentai_benchmark/17.mp4" video = video_to_ndarrays(video_path, n...

## 现有链接修复摘要

#27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: process audios in pass audio in video with qwen2.5-omni-7b bug ### Your current environment ### 🐛 Describe the bug another bug when i test single video with audio. After process the audio, the dimension of "input...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: " f"{question} \n" f" assistant\n" ) # from test import load_dataset # import os # saved_dataset_path = "dataset.pkl" # if os.path.exists(saved_dataset_path): # print(f"Found saved dataset at {saved_dataset_path}, loadi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Your current environment ### 🐛 Describe the bug another bug when i test single video with audio. After process the audio, the dimension of "input_features" and "feature_attention_mask" doesn't match. The video exceeds t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape #27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27721](https://github.com/vllm-project/vllm/pull/27721) | closes_keyword | 0.95 | [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.   | FIX #22364 CLOSE #23888 CLOSE #25473 CLOSE https://github.com/vllm-project/vllm/issues/28046 ## Test Plan ``` HF_HUB_DISABLE_XET=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA python example |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
