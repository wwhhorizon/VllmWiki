# vllm-project/vllm#24992: [Bug]: Empty VllmConfig when initializing LogitsProcessor

| 字段 | 值 |
| --- | --- |
| Issue | [#24992](https://github.com/vllm-project/vllm/issues/24992) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty VllmConfig when initializing LogitsProcessor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Recent changes to `LogitsProcessor` added custom Ops support to it. `@CustomOp.register("logits_processor")` ([REF](https://github.com/vllm-project/vllm/pull/23564)) While initializing `LogitsProcessor`, the `CustomOp` init is called which calls `get_current_vllm_config` before `set_current_vllm_config` is even invoked. As a result, `get_current_vllm_config` initializes an empty `VllmConfig` and calls `check_and_update_config` step. In a custom plugin, when accessing fields like `vllm_config.model_config.max_model_len`, an error is thrown. Code: I edited this file and added an assert: `tests/plugins/vllm_add_dummy_platform/vllm_add_dummy_platform/dummy_platform.py`: ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project from typing import TYPE_CHECKING from vllm.platforms.interface import Platform, PlatformEnum if TYPE_CHECKING: from vllm.config import VllmConfig else: VllmConfig = None from vllm import envs class DummyPlatform(Platform): _enum = PlatformEnum.OOT device_name = "DummyDevice" device_type: str = "privateuseone" dispatch_key: str = "PrivateUse1" @classmeth...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ileCopyrightText: Copyright contributors to the vLLM project from typing import TYPE_CHECKING from vllm.platforms.interface import Platform, PlatformEnum if TYPE_CHECKING: from vllm.config import VllmConfig else: VllmCo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e: str = "privateuseone" dispatch_key: str = "PrivateUse1" @classmethod def check_and_update_config(cls, vllm_config: VllmConfig) -> None: if envs.VLLM_USE_V1: compilation_config = vllm_config.compilation_config # Activ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: device_name = "DummyDevice" device_type: str = "privateuseone" dispatch_key: str = "PrivateUse1" @classmethod def check_and_update_config(cls, vllm_config: VllmConfig) -> None: if envs.VLLM_USE_V1: compilation_config =...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: PlatformEnum if TYPE_CHECKING: from vllm.config import VllmConfig else: VllmConfig = None from vllm import envs class DummyPlatform(Platform): _enum = PlatformEnum.OOT device_name = "DummyDevice" device_type: str = "pri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Empty VllmConfig when initializing LogitsProcessor bug;stale ### Your current environment ### 🐛 Describe the bug Recent changes to `LogitsProcessor` added custom Ops support to it. `@CustomOp.register("logits_pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
