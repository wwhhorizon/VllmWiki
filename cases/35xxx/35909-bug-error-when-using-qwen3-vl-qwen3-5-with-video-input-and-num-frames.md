# vllm-project/vllm#35909: [Bug]: Error when using Qwen3-VL/Qwen3.5 with video input and num_frames

| 字段 | 值 |
| --- | --- |
| Issue | [#35909](https://github.com/vllm-project/vllm/issues/35909) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when using Qwen3-VL/Qwen3.5 with video input and num_frames

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I found a bug in the [Qwen3-VL model executor](https://github.com/vllm-project/vllm/blob/97995f6376fd3dae7a67624055ddf038233e181e/vllm/model_executor/models/qwen3_vl.py#L1055) when using **`num_frames`** via `mm_processor_kwargs` in `LLM.chat()` / `LLM.generate()`. ## What happens I have observed that when passing `num_frames` in `mm_processor_kwargs` from `ll.chat()` or `generate()` methods, an error is raised from [qwen3_vl.py model executor](https://github.com/vllm-project/vllm/blob/97995f6376fd3dae7a67624055ddf038233e181e/vllm/model_executor/models/qwen3_vl.py#L1055): ```text assert len(timestamps) == grid_thw[0], ( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError: The timestamps length(10) should be equal video length (16). ``` The error is triggered around [this part](https://github.com/vllm-project/vllm/blob/97995f6376fd3dae7a67624055ddf038233e181e/vllm/model_executor/models/qwen3_vl.py#L1060-L1062), where the executor reads `fps` from `hf_processor_mm_kwargs`: ```python video, metadata = mm_items["video"][item_idx] do_sample_frames = hf_processor_mm_kwargs.get("do_sample_frames") sampled_fps = hf_processor_mm_kwargs.get(...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Error when using Qwen3-VL/Qwen3.5 with video input and num_frames bug ### Your current environment ### 🐛 Describe the bug Hi, I found a bug in the [Qwen3-VL model executor](https://github.com/vllm-project/vllm/bl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oduce I’m including a minimal repro snippet below: ```python from vllm import LLM, SamplingParams if __name__ == '__main__': checkpoint_path = "Qwen/Qwen3-VL-8B-Instruct" llm = LLM( model=checkpoint_path, media_io_kwarg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s/models/qwen3_vl/video_processing_qwen3_vl.py#L95)). This produces a mismatch between the reconstructed `timestamps` length and the number of frames represented by `video_grid_thw` (which reflects the `num_frames` valu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: model=checkpoint_path, media_io_kwargs={"video": {"video_backend": "opencv", "num_frames": -1}}, allowed_local_media_path=" ", seed=0, ) sampling_params = SamplingParams( temperature=0.7, top_p=0.8, top_k=20, max_tokens=
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ers/models/qwen3_vl/video_processing_qwen3_vl.py#L95)). This produces a mismatch between the reconstructed `timestamps` length and the number of frames represented by `video_grid_thw` (which reflects the `num_frames` va...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
