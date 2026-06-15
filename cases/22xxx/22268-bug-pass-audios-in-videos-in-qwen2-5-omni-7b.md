# vllm-project/vllm#22268: [Bug]: pass audios in videos in qwen2.5-omni-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#22268](https://github.com/vllm-project/vllm/issues/22268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pass audios in videos in qwen2.5-omni-7b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I try to get the outputs of inputs 6-9, it exits following error(adding inputs 7), missing audio but if I try to get the ouputs of inputs 4-6, 7-9 respectively, it works normally.(4-6processed prompt oom but add requests succeed) ```python def load_data(data_path: str): # Walk through the directory structure dataset_with_audio = [] dataset_without_audio = [] num_files = 0 for root, dirs, files in os.walk(data_path): for file in files: if file.endswith('.json'): # Process each JSON file json_file_path = os.path.join(root, file) try: with open(json_file_path, 'r') as f: data = json.load(f) # Handle both single item and list of items if isinstance(data, list): items = data else: items = [data] for item in tqdm(items): video_path = item.get("video_path") labels = item.get("labels", []) if video_path: try: # Handle relative and absolute paths root_path = os.path.dirname(data_path) video_path = os.path.join(root_path, video_path) if os.path.exists(video_path): video = video_to_ndarrays(video_path, num_frames=32) try: audio = librosa.load(video_path, sr=16000)[0] dataset_with_audio.append({ "video": video, "audio": audio, "labels":...

## 现有链接修复摘要

#27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: pass audios in videos in qwen2.5-omni-7b bug;stale ### Your current environment ### 🐛 Describe the bug when I try to get the outputs of inputs 6-9, it exits following error(adding inputs 7), missing audio but if...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: pass audios in videos in qwen2.5-omni-7b bug;stale ### Your current environment ### 🐛 Describe the bug when I try to get the outputs of inputs 6-9, it exits following error(adding inputs 7), missing audio but if...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;oom env_dependency;shape #27721 [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 en...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27721](https://github.com/vllm-project/vllm/pull/27721) | closes_keyword | 0.95 | [Multimodal][Qwen3 Omni] Make Qwen3 Omni work with audio-in-video inputs in V1 engine.   | FIX #22268 FIX #22364 CLOSE #23888 CLOSE #25473 CLOSE https://github.com/vllm-project/vllm/issues/28046 ## Test Plan ``` HF_HUB_DISABLE_XET=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA pyt |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
