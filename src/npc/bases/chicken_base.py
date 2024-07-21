from __future__ import annotations

from abc import ABC

import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from src.npc.bases.animal import Animal
from src.npc.behaviour.ai_behaviour import AIBehaviour
from src.settings import Coordinate, AniFrames


class ChickenBase(Animal, AIBehaviour, ABC):
    def __init__(
            self,
            pos: Coordinate,
            frames: dict[str, AniFrames],
            groups: tuple[pygame.sprite.Group, ...],
            collision_sprites: pygame.sprite.Group,

            pf_matrix: list[list[int]],
            pf_grid: Grid,
            pf_finder: AStarFinder,

            z: int
    ):
        Animal.__init__(
            self,
            pos=pos,
            frames=frames,
            groups=groups,
            collision_sprites=collision_sprites,

            shrink=(30, 30),

            z=z
        )
        AIBehaviour.__init__(
            self,
            pf_matrix=pf_matrix,
            pf_grid=pf_grid,
            pf_finder=pf_finder
        )

        self.speed = 250