# vllm-project/vllm#25944: [Bug]: Qwen3_omni demo error as below

| 字段 | 值 |
| --- | --- |
| Issue | [#25944](https://github.com/vllm-project/vllm/issues/25944) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3_omni demo error as below

### Issue 正文摘录

### Your current environment I am trying to use the Qwen3_omni web demo as below `https://github.com/QwenLM/Qwen3-Omni/blob/main/web_demo.py` executing the file with instruct or thinking model as below `https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct` with locally offline downloaded and using the transformers model directly installed from git version 4.57.0.dev and below is the error. `model = LLM( [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 282, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 493, in from_engine_args [rank0]: return engine_cls.from_vllm_config( [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 469, in from_vllm_config [rank0]: return cls( [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 260, in __init__ [rank0]: self.model_executor = executor_class(vllm_config=vllm_config) [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packages/vllm/executor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: Qwen3_omni demo error as below bug ### Your current environment I am trying to use the Qwen3_omni web demo as below `https://github.com/QwenLM/Qwen3-Omni/blob/main/web_demo.py` executing the file with instruct or...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ith locally offline downloaded and using the transformers model directly installed from git version 4.57.0.dev and below is the error. `model = LLM( [rank0]: File "/home/user/allwork/envs/omni3/lib/python3.10/site-packa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nfig, BioGptConfig, BitConfig, BitNetConfig, BlenderbotConfig, BlenderbotSmallConfig, BlipConfig, Blip2Config, Blip2QFormerConfig, BloomConfig, BltConfig, BridgeTowerConfig, BrosConfig, CamembertConfig, CanineConfig, Ch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Config, Emu3Config, EncodecConfig, ErnieConfig, Ernie4_5Config, Ernie4_5_MoeConfig, ErnieMConfig, EsmConfig, EvollaConfig, Exaone4Config, FalconConfig, FalconH1Config, FalconMambaConfig, FastSpeech2ConformerConfig, Fast...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: g, BlenderbotSmallConfig, BlipConfig, Blip2Config, Blip2QFormerConfig, BloomConfig, BltConfig, BridgeTowerConfig, BrosConfig, CamembertConfig, CanineConfig, ChameleonConfig, ChineseCLIPConfig, ChineseCLIPVisionConfig, C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
